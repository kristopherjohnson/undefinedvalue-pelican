Title: F#'s Pipe-Forward Operator in Swift
Date: 2014-07-14 01:09:09
Category: Blog
Slug: fs-pipe-forward-operator-swift
Alias: 2014/07/13/fs-pipe-forward-operator-swift/
Tags: swift, iosdev, functionalprogramming, fsharp


*Note: At WWDC 2015, Apple announced Swift 2, which includes changes and a new feature called "protocol extensions" that render much of the code below either irrelevant or incorrect. This article applies to Swift 1.x.*

Apple's new [Swift](https://developer.apple.com/swift/) programming language isn't really a [functional programming language](http://en.wikipedia.org/wiki/Functional_programming). However, it does support generic types and functional-programming patterns, so many FP aficionados are implementing their favorite functional idioms and libraries from other programming languages in Swift.

I've been a functional-programming enthusiast for a couple of decades, and I'm playing with this myself. A feature I like in the [F# programming language](http://en.wikipedia.org/wiki/F_Sharp_(programming_language)) is its [pipe-forward operator](http://www.kevinberridge.com/2012/12/neat-f-pipe-forward.html), `|>`, which helps to write readable functional code. This article explains what that operator is, why you would want to use it, and how to do it in Swift.

Disclaimer: The code in this article is based upon the versions of the Swift language in Xcode 6.3. Future changes to Swift syntax or its standard library may render all of this incorrect or obsolete.
<!--break-->
## Life without pipe-forward

Before describing pipe-forward, let's look at an example that demonstrates why we might want it. Say we need to write code that takes an array of integers, filters out the odd numbers, sorts the remaining even numbers in descending order, and then renders the result as a string of comma-separated numbers. Using methods of Swift's [Array](https://developer.apple.com/library/prerelease/ios/documentation/General/Reference/SwiftStandardLibraryReference/Array.html#//apple_ref/doc/uid/TP40014608-CH5-SW1) and [String](https://developer.apple.com/library/prerelease/ios/documentation/General/Reference/SwiftStandardLibraryReference/index.html#//apple_ref/doc/uid/TP40014608-CH7-SW1) classes, we could do it like this:

    let numbers = [67, 83, 4, 99, 22, 18, 21, 24, 23, 2, 86]

    let result = ", ".join(numbers.filter { $0 % 2 == 0 }
                                  .sorted { $1 < $0 }
                                  .map { $0.description })

The value of `result` is the string `"86, 24, 22, 18, 4, 2"`.

That `result` expression might be a little complicated, but at a glance it is easy to see that it filters the numbers,  sorts them, maps the values to strings, and then uses `String.join()` to construct the result.

If you aren't familiar with using `map` and `filter` to transform collections, read [the Cocoaphony article](http://robnapier.net/maps).

Now what if, instead of an _array_ of numbers, we have a _sequence_ of numbers? A sequence doesn't have methods like `Array` does. Instead we will have to use the `filter()`, `sorted()`, and `map()` free functions provided by the Swift standard library. If we try to write the code as a single expression like we did above, we end up with something like this:

    let seq = SequenceOf(numbers)

    let seqResult =
        ", ".join(map(sorted(filter(seq){$0 % 2 == 0}){$1 < $0}){$0.description})

or like this:

    let seqResultMultiLine =
        ", ".join(
            map(
                sorted(
                    filter(seq) { $0 % 2 == 0 }
                ) { $1 < $0 }
            ) { $0.description })

That's not very readable, is it? We can see at a glance that `filter`, `map`, `sorted`, and `join` are being used, but we have to read it inside-out and backwards to follow the order of evaluation and figure out which closure goes with which function call and how the data is flowing through those functions. We probably wouldn't even try to write it as a single expression, and would instead write it as a sequence of intermediate results to make it understandable:

    let filteredNumbers = filter(seq) { $0 % 2 == 0 }
    let sortedNumbers = sorted(filteredNumbers) { $1 < $0 }
    let numbersAsStrings = map(sortedNumbers) { (n: Int) -> String in n.description }
    let commaSeparatedResult = ", ".join(numbersAsStrings)

That's easier to understand, but it's noisier than the original `Array`-based code.

## Life with pipe-forward

Wouldn't it be nice if we could call a function on a value using a postfix notation like we call a method on an object? That is, wouldn't it be nice if we could write something like this?

    let pipeResult =
        seq |> filteredWithPredicate { $0 % 2 == 0 }
            |> sortedByPredicate { $1 < $0 }
            |> mappedWithTransform { $0.description }
            |> String.join(", ")

We can. That `|>` operator is called the "pipe-forward" or "forward pipe" operator in F#.

This:

    x |> f

is equivalent to this:

    f(x)

and this:

    x |> f |> g |> h

is equivalent to this:

    h(g(f(x)))

It's just syntactic sugar, but it is often clearer to express a sequence of function calls as a chain read left-to-right/top-to-bottom than as a cluster of nested subexpressions.

It can be defined as an operator in Swift like this:

    infix operator |>   { precedence 50 associativity left }

    public func |> <T,U>(lhs: T, rhs: T -> U) -> U {
        return rhs(lhs)
    }

We have some work to do before we can evaluate `pipeResult` above with our `|>` operator. The problem is that the `filter()`, `sorted()`, and `map()` functions provided by the Swift standard library don't have their parameters in the order we need, and they are not written to support [partial application](http://en.wikipedia.org/wiki/Partial_application).  For example, let's look at the first subexpression:

    seq |> filteredWithPredicate { $0 % 2 == 0 }

The pipe-forward operator transforms it to this:

    filteredWithPredicate({ $0 % 2 == 0 })(seq)

So we need `filteredWithPredicate` to be a [curried function](https://developer.apple.com/library/prerelease/ios/documentation/Swift/Conceptual/Swift_Programming_Language/Declarations.html#//apple_ref/doc/uid/TP40014097-CH34-XID_591) that takes the predicate as the first argument and sequence as second argument. Unfortunately, the library's `fillter/sorted/map` functions are not curried and are called with the sequence as the first argument and function as second argument.  To make the `pipeResult` expression compile and run, we need to provide some "adapter functions" that have the necessary signatures:

    // Curried adapter function for Swift Standard Library's filter() function
    public func filteredWithPredicate<S : SequenceType>
        (includeElement: (S.Generator.Element) -> Bool)
        (source: S)
        -> [S.Generator.Element]
    {
        return filter(source, includeElement)
    }

    // Curried adapter function for Swift Standard Library's sorted() function
    public func sortedByPredicate<S : SequenceType>
        (predicate: (S.Generator.Element, S.Generator.Element) -> Bool)
        (source: S)
        -> [S.Generator.Element]
    {
        return sorted(source, predicate)
    }

    // Curried adapter function for Swift Standard Library's map() function
    public func mappedWithTransform<S: SequenceType, T>
        (transform: (S.Generator.Element) -> T)
        (source: S)
        -> [T]
    {
        return map(source, transform)
    }

These adapter declarations may look complicated, but all we did was copy the signatures of the original functions, then curry the parameters and reverse their order.

Note that we don't need to write an adapter function to use the `String.join()` method, because instance methods of structs and classes can be used as curried functions. See [Ole Begemann's article](http://oleb.net/blog/2014/07/swift-instance-methods-curried-functions/) for more details.

With those adapter function declarations, the `pipeResult` expression works as expected. Complete code that can be pasted into a Swift playground is available here: <https://gist.github.com/kristopherjohnson/ed97acf0bbe0013df8af>

It might seem like we have done a _lot_ of work just to have a pretty-looking filter-sort-map-reduce expression, but thanks to generic types, all of the above can be reused wherever we need it.  All our data-processing code can look like simple transformation pipelines, and that's worth the effort.

In Microsoft's Visual Studio, if you are writing F# code and you type `|>`, the IDE pops up an auto-completion list of all the functions that can be applied to the value on the left, just like typing a `.` after an object brings up a list of its methods and properties. Xcode can do this too, but without `|>` being a standard Swift operator, few developers will be able to take advantage of it. If you think `|>` and functional auto-complete would be a useful addition to Swift and Xcode, you can submit a bug report to Apple requesting it. (You can [dupe my radar](http://www.openradar.me/radar?id=5837161337192448).)


## Optional chaining

What if we have functions that return Optionals, and want to pipe those to functions that take non-Optional values? We can define a couple of operators to handle those cases:

    infix operator |>!  { precedence 50 associativity left }
    infix operator |>&  { precedence 50 associativity left }

    public func |>! <T,U>(lhs: T?, rhs: T -> U) -> U {
        return rhs(lhs!)
    }

    public func |>& <T,U>(lhs: T?, rhs: T -> U) -> U? {
        return lhs.map(rhs)
    }

The `|>!` operator unwraps its left-side argument and passes it to the function on the right. This is safe if we know that the Optional value will never be nil.

The `|>&` operator checks whether the left-side argument is `nil`. If so, the value of the expression is `nil`. If not, then the Optional is unwrapped and the right-side function is applied to it. (I'd rather name this operator `|>?`, but Swift doesn't allow the `?` character in operator names.)  This is the same as just calling `Optional.map()`, but if we are using a pipeline it is useful to use just pipe operators rather than mixing pipes and method calls.

Here are some simple usage examples, using the Swift Standard Library's `find()` function, which returns an `Int?` which is the index of the searched-for value, or `nil` if not found:

    let elements = [2, 4, 6, 8, 10]

    func reportIndexOfValue(value: Int)(index: Int) -> String {
        let message = "Found \(value) at index \(index)"
        println(message)
        return message
    }

    find(elements, 6) |>! reportIndexOfValue(6)    // "Found 6 at index 2"

    find(elements, 3) |>& reportIndexOfValue(3)    // nil
    find(elements, 4) |>& reportIndexOfValue(4)    // {Some "Found 4 at index 1"}


## Functions with multiple parameters, and tuples

It might seem that the pipe-forward operator is only useful when passing an argument to a function that takes a single parameter. However, a Swift function can be applied to a tuple of arguments, so you can use a tuple on the left side of `|>` and a function taking multiple arguments on the right side.

In other words, this:

    (x, y, z) |> f

is equivalent to this:

    f(x, y, z)

For example:

    import Foundation

    func diagonalLength(width: Double, height: Double) -> Double {
        return sqrt(width * width + height * height)
    }

    let length = (3, 4) |> diagonalLength                     // result is 5.0

    func multiplyAndDivide(multiplier1: Double, multiplier2: Double, divisor: Double) -> Double {
        return multiplier1 * multiplier2 / divisor
    }

    let value = (10, 20, 50) |> multiplyAndDivide         // result is 4.0

These can be useful in more complex pipeline expressions that require use of tuples as arguments, results, or intermediate values. We can use [zip() or zip3()](https://gist.github.com/kristopherjohnson/04dbc470e17f67f836a2) to combine values from other sequences into tuples to be piped into functions.

You could even do something like this:

    let evenNumbers = (seq, { $0 % 2 == 0 }) |> filter

That seems unnecessarily weird in isolation, but it may be useful in the context of a larger pipe expression.

## For more

Martin Fowler's [Collection Pipeline](http://martinfowler.com/articles/collection-pipeline/) article is a good overview of the general pattern, with examples in multiple programming languages.

For more about F#'s pipe-forward operator and related operators, see the "Function Composition and Pipelining" section of this page: <http://msdn.microsoft.com/en-us/library/dd233229.aspx>

[@AirspeedSwift](https://twitter.com/airspeedswift) has some advanced examples of using pipe-forward with other FP techniques in Swift. See these articles:

- [A straw man argument for trying more functional-style programming in Swift](http://airspeedvelocity.net/2014/12/03/a-straw-man-argument-for-more-trying-functional-programming-in-swift/)
- [zipWith, pipe forward, and treating functions like objects](http://airspeedvelocity.net/2014/12/05/zipwith-pipe-forward-and-treating-functions-like-objects/)

## Acknowledgements

Thanks to [Greg Titus](https://twitter.com/gregtitus) and [Rob Napier](https://twitter.com/cocoaphony) for assistance and critique.

## Afterword

The above was originally written with an early beta of Swift. As of Xcode 6 beta 4, the Swift standard library provides a `lazy()` function that transforms a sequence into an object that has lazily evaluated `filter()` and `map()` methods, so we could solve the problem like this:

    let lazyResult =
        ", ".join(lazy(seq).filter({ $0 % 2 == 0 }).array
                           .sorted({$1 < $0})
                           .map { $0.description })

I still prefer the `pipeResult` expression. I think it looks more like a data-flow illustration. The lazy version has some excess noise (`lazy()`, `.array`), and it may be even more mystifying to non-functional programmers than the pipeline notation is.

<h2 id="pipeAdapted">Another afterword</h2>

Above, after the definitions of the "adapter functions", I wrote "all we did was copy the signatures of the original functions, then curry the parameters and reverse their order." That seems like something we should be able to do with a higher-level function, right?

    // Given a function with signature (A, B) -> T, return curried
    // function with signature (B)(A) -> T
    func pipeAdapted<A, B, T>(f: (A, B) -> T) -> (B -> A -> T) {
        return { b in { a in f(a, b) } }
    }

    let pipeAdaptedResult =
        seq |> pipeAdapted(filter)({ $0 % 2 == 0 })
            |> pipeAdapted(sorted)({ $1 < $0 })
            |> pipeAdapted(map)({ $0.description })
            |> String.join(", ")

Here, we use a `pipeAdapted()` function to transform the standard library's `filter`, `sorted`, and `map` functions into what we need, instead of writing those adapters. If you and your team members are all FP ninjas who don't bat an eye at throwing functions around, then you may prefer this, but my preference is still for the version that uses the adapter functions.

An alternative that may be a little more palatable to non-FP people is to define another pipe operator that lets us specify a function and predicate, like so:

    infix operator |>*  { precedence 50 associativity left }

    // Transform "x |>* (f, predicate)" to "f(x, predicate)"
    public func |>* <A, B, C, T>(lhs: A, rhs: ((A, (B) -> C) -> T, (B) -> C)) -> T {
        return (rhs.0)(lhs, rhs.1)
    }

    let pipeStarResult =
        seq |>* (filter, { $0 % 2 == 0 })
            |>* (sorted, { $1 < $0 })
            |>* (map, { $0.description })
            |> String.join(", ")

Note that a big problem with either of these approaches is that the Swift compiler takes a very, very, VERY long time to compile them, presumably due to a combinatorial explosion in the type-inferencing mechanism with all those generic types. This may be a temporary issue that will be resolved as the Swift compiler matures, but for now, it's hard to recommend these approaches for general-purpose use.

We can hope that a future version of Swift will provide better built-in support for curried functions and partial application.

Finally, one could skip all this "currying" and "adapter" business and use some closures to define ad-hoc anonymous functions that can be applied to sequences in a pipeline:

    let closuresResult =
        seq |> { s in filter(s) { $0 % 2 == 0 } }
            |> { s in sorted(s) { $1 < $0 } }
            |> { s in map(s) { $0.description } }
            |> String.join(", ")

I still find something like this hard to read, but with more FP-in-Swift experience, it may be as clear as `pipeResult`. And thankfully, it compiles quickly.

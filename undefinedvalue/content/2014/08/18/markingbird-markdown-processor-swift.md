Title: Markingbird: A Markdown Processor for Swift
Date: 2014-08-18 12:43:35
Category: Blog
Slug: markingbird-markdown-processor-swift
Alias: 2014/08/18/markingbird-markdown-processor-swift/
Tags: swift, markingbird, markdown, iosdev


[Markingbird](https://github.com/kristopherjohnson/Markingbird) is a [Markdown](http://daringfireball.net/projects/markdown/) processor written in [Swift](https://developer.apple.com/swift/) for OS X and iOS. It is a translation/port of the [MarkdownSharp](https://code.google.com/p/markdownsharp/) processor used by the [Stack Overflow](http://blog.stackoverflow.com/2009/12/introducing-markdownsharp/) website.

(If you have no idea what "Markdown" and "Swift" are, you can just stop reading now.)
<!--break-->
Repository: <https://github.com/kristopherjohnson/Markingbird>

See the [README](https://github.com/kristopherjohnson/Markingbird/blob/master/README.md) for details on how to use it, and some of the details of how the C# code was translated to Swift.

I can't claim much credit for this project. It is really just a line-by-line translation of [Jeff Atwood's C# code](http://blog.stackoverflow.com/2009/12/introducing-markdownsharp/) into Swift. The result is not very pretty, as the C# code is itself based upon translations of Perl and PHP code. I don't recommend this as an example of how to write Swift code, but it does seem to work, and so I hope it is valuable to somebody someday.

This project was useful to me in that it let me write a lot of Swift code without thinking too much about it. It helped me develop Swift-editing muscle memory, quick scanning and correction of Swift syntax issues, and interpretation of the Swift compiler's not-always-helpful error messages. I thought about giving up a few times, as manual translation of 1,800 lines of C# and regular expressions wasn't a great way to spend nights and weekends, but I just couldn't leave it partially finished.

I did the translation by just copying and pasting the C# code into Xcode, and then fixing whatever was wrong. This was a real workout for Xcode 6 beta 5, as the SourceKitService or Xcode itself would often crash or lock up when it encountered C# code.

The most annoying and fiddly part of the process was translating the C# regular-expression strings into Swift. It would be nice if Swift had a "raw" string literal like other languages do, but it doesn't, so I manually transformed each regular expression into a Swift/NSRegularExpression-compatible form. Sublime Text's multiple-selection feature was really helpful for this. I probably could have written some sort of a script to automate the translations, but actually looking at every line was valuable in finding edge cases.

I also discovered a few differences between .NET regular expressions and Cocoa regular expressions. For example, in .NET you can use `[ ]` (a single space between square brackets) to mean a single space, but `NSRegularExpression` won't accept this, so I had to use `\\p{Z}` instead. Also, if a regular expression pattern ends with a `|` character, .NET apparently ignores it, but `NSRegularExpression` just lets it match empty strings.

Some of the messiest code that I wrote myself (rather than simply translating) is code that manipulates individual characters and substrings. Swift's `String` type can make this difficult, due to its extensive Unicode support, so I found myself going back and forth between using `String` and `NSString` for string manipulation. The automatic bridging between those two types provided by Swift makes it pretty easy, but it would be nice if somebody made a library of utility functions for dealing with `String`. (BTW, I strongly recommend that all Swift programmers read Ole Begemann's [Strings in Swift](http://oleb.net/blog/2014/07/swift-strings/) article to find out what's going on with `String`.)

As of now, the `SimpleTests` test suite from MarkdownSharp works. I plan to port the remaining unit tests from MarkdownSharp, and add a few tests of my own. There are also a few TODOs left in the code that need to be addressed.

I make no promises about the robustness or performance of Markingbird. If you find problems, please submit issues and pull requests via GitHub.

I know some people will want to tell me that using regular expressions for this is bad, and this should be a real parser written in pure Swift. I agree completely: let me know when you have implemented that, and I'll post links to it.

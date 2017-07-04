Title: What I've Learned about iOS Development
Date: 2011-03-29 03:43:00
Category: Blog
Slug: what-ive-learned-about-ios-development
Alias: 2011/03/28/what-ive-learned-about-ios-development/
Tags: iphone, ipad, iosdev


I've been playing around with development for Mac OS X and iOS for a few years. I've had a pretty good grasp of how Cocoa and UIKit worked, and I've written some simple apps, but for the past month I've been working on my first _Real iOS Application_. I've had to solve some problems that were easily ignored when writing little apps for fun. What follows is a randomly ordered collection of some of the little techniques and tips I didn't know before, which may be useful for other Cocoa newbies.
<!--break-->
(More to come as I learn from more mistakes.)


## NSDictionary is Incredibly Useful

As a long-time C++ programmer, whenever I have some sort of "object" with a bunch of "attributes" my instinct is to define a `class` or `struct` with a bunch of instance members. However, when using Objective-C, it is often easier and more useful to just throw all that stuff into an `NSDictionary` (or `NSMutableDictionary`), for the following reasons:

- You don't have to write code to save/load the data to/from files or `NSUserDefaults`. As long as you can live with `NSDictionary`'s serialization format, you get persistence for free.
- Many system classes and APIs already know how to work with dictionaries in interesting ways.
- It's easier than defining an Objective-C class with properties. I know some Objective-C fans will disagree, but the `@property` mechanism sucks. If you use an `NSDictionary`, then you can worry less about retain counts, `dealloc`, and other such things.
- It lets you write JavaScript-like or Python-like code, if you're into that sort of thing.

The downside of using `NSDictionary` is that it may be less efficient than using a custom class or a `struct`. Use your brain.


## Use NSValue to Box Pointers and Primitives

If you follow the above advice about using `NSDictionary`, you'll run into a couple of wrinkles with using it as a general-purpose attribute container:

- Keys and values have to be objects, not primitive types.
- The keys have to conform to the `NSCopying` protocol.
- The dictionary will retain values, which may introduce undesirable retain cycles.

The workaround for these issues is to use the `NSValue` class and its subclasses, which can box most interesting values as objects that can be used as dictionary keys and values.

`+[NSValue valueWithNonretainedObject:]` is how you put objects into your collections without bumping the retain counts.


## Use objc_setAssociatedObject() and objc_getAssociatedObject() to Extend Unsubclassable Classes

The Apple frameworks contain some classes which cannot be subclassed (or cannot be _easily_ subclassed). If you just want to add some methods, then you can just define a category. In cases where you wish you could make a subclass to add a property or two, the workaround is to use `objc_setAssociatedObject()` and `objc_getAssociatedObject()`.


## Don't Support Old iOS Versions If You Don't Absolutely Have To

I'm lucky in that I am developing an in-house application, not to be sold in the App Store, so I was able to decree that I would only support devices running iOS 4.2 and higher. This lets me take advantage of useful stuff that isn't available in pre-4.0 versions of iOS without cluttering the code with a lot of checks for feature support. It's nice to use blocks and regular expressions and other "new" iOS features without worrying about it.

Even if I was developing for the App Store, I'd be tempted to require 4.0. People who haven't bought a new phone for a few years or who don't keep the OS up to date aren't going to pay for that app you're developing, so why do anything for them?


## Don't Mix Objective-C and C++ Unnecessarily

For a while, I was enamored with "Objective-C++", which is what you get when you change your `.m` suffixes to `.mm` and put C++ code into your Objective-C code. I thought this would be nifty, because I could use cool stuff from C++ (templates, typesafe container classes, smart pointers, RAII, ...).

I did this for a while, but found that every time I decided to rewrite the C++ parts in plain-old-idiomatic Objective-C, the result was cleaner. So I don't do it any more.

 I think use of Objective-C++ is best limited to cases where you need to integrate some existing C++ code or libraries into your app, or when the guts of the app are all written in C++ and you need to interface with Objective-C-based UI classes. Don't use it to "improve" Objective-C. Objective-C is already a clumsy combination of C and Smalltalk. Dumping a third language into the mix doesn't make it better.


## Use the Static Analyzer

Objective-C's manual memory management sucks, but I have yet to see a memory leak in my app that wasn't caught by the static analyzer. Run that Analyze command once in a while.


## You Don't Have to Use Interface Builder

I spent a long time struggling with figuring out how to do complicated things in Interface Builder (like laying out a tab bar with a set of navigation controllers, each with toolbar items in their button bars and ...). After all, this is how one creates GUIs on other platforms.

IB can be helpful, particularly when laying out a form-style view, but in many cases it is easier to create your views and hook up the events by writing code.

I'm not saying "Don't use Interface Builder," or "Interface Builder is for pussies." I'm just saying that if you know how to do it all in code, it will often be easier to get what you want.


## Use UIWebView for Read-Only Views

For a view that simply displays information, it is often easier to write some simple HTML and CSS and display it in a UIWebView than it is to lay out a bunch of UIKit components. It also gives your non-Objective-C-knowing colleagues a way to help you out (but don't let them use Arial).


## Use Xcode 4

At the time of this writing, Xcode 4 is new (released just a few weeks ago), and lots of people are having problems with it. Those people recommend sticking with Xcode 3.x until the problems get worked out.

If you run into those problems, or if you are an old-timer who fears change, then by all means, use Xcode 3. But if you can use Xcode 4, then I heartily recommend it. The improved autocompletion alone is worth the risk of crashes and hiccups.

Xcode 4 is pretty rough for a released Apple product, but iIt really isn't that bad. When I first started using, it seemed like it was crashing "all the time." I started recording each crash, and found that over the course of three weeks it crashed, on average, only about once per day. The crashes are annoying, but the effect on my productivity was neglible. YMMV.


## Use Ingredients

The Xcode documentation viewer sucks. Install [Ingredients](http://fileability.net/ingredients/). It's free. Assign a keyboard shortcut to the _Look up in Ingredients_ item in the Services menu.


## Use TBXML for XML Parsing

I experimented with a few XML parsers, and settled on [TBXML](http://www.tbxml.co.uk/TBXML/TBXML_Free.html) as my preferred parser. It's got the best combination of performance and ease of use.

However, it is not necessarily the best for all purposes. See [How to Choose the Best XML Parser for Your iPhone Project](http://www.raywenderlich.com/553/how-to-chose-the-best-xml-parser-for-your-iphone-project) for a survey of available XML parsers.

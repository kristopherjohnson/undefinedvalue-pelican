Title: The Good Old Days and Tiny BASIC
Date: 2014-12-21 02:14:03
Category: Blog
Slug: good-old-days-and-tiny-basic
Alias: 2014/12/20/good-old-days-and-tiny-basic/
Tags: tinybasic, swift, basic


This week, we learned that [_Dr. Dobb's Journal_ is shutting down after 38 years](http://www.drdobbs.com/architecture-and-design/farewell-dr-dobbs/240169421). Admittedly, I haven't paid much attention to _Dr. Dobb's_ for the past few years, but back when I was a kid who wanted to be a programmer, I anxiously awaited each monthly issue so that I could read every single article multiple times. We didn't have the Internet to give us whatever training we needed whenever we wanted, so magazines like _Dr. Dobb's_ were precious.

While reminiscing about _Dr. Dobb's_ with other grieving Twitter users, somebody brought up the fact that the first issue was titled ["Dr. Dobb's Journal of Tiny BASIC Calisthenics & Orthodontia: Running Light Without Overbyte"](http://www.drdobbs.com/architecture-and-design/sourcecode/dr-dobbs-journal-30/30000144)  (which I think is the coolest magazine title I've ever heard). It started as a xerographed newsletter to tell people about [_Tiny BASIC_](http://en.wikipedia.org/wiki/Tiny_BASIC), a simplified [BASIC programming language](http://en.wikipedia.org/wiki/BASIC) interpreter that could run in 2 or 3 kilobytes of memory. That was an important feature back when personal computers had only 4 kilobytes of memory.

Having just completed an implementation of a [Forth programming language interpreter](https://github.com/kristopherjohnson/suwaneeforth) in Apple's new [Swift](https://developer.apple.com/swift/) programming language, I got the idea of implementing a Tiny BASIC interpreter in Swift. It didn't make any sense. I didn't want to write any programs in Tiny BASIC. I didn't think anybody else would want to write any programs in Tiny BASIC. There are more important things I could be doing with my free time.

But, apparently, reimplementing 50-year-old programming languages in Swift is my thing now

I did it. I call it "Finch", and if you want it, you can find it here:

- https://github.com/kristopherjohnson/FinchBasic

Useless as it may be, it was an interesting exercise. Most of the Tiny BASIC implementations you find are focused on the original goal: getting a full implementation to fit in a few kilobytes. That isn't an important goal anymore, but I liked the idea of implementing a very-simple programming language. I focused on these goals:

- Use Swift's high-level abstraction features, rather than writing code that looks like C or assembly language.
- Make it easy for new Swift programmers to understand, so it could be useful as a beginner's example or in a tutorial.
- Make it easy for people to hack on to add new features.

I think I did alright. It's about a thousand lines of code (not counting blank lines and comments), which is smaller than a [C-based Tiny BASIC implementation](http://www.ittybittycomputers.com/IttyBitty/TinyBasic/TinyBasic.c) I found, and I don't think I did anything too complicated. I will have to wait and see if anyone else wants to hack on it.

BASIC was the first programming language I learned. I expressed an interest in programming after attending an IBM open house, and my father brought home a BASIC programming manual. I studied it intently, but there weren't any computers around, so it was a while before I could try out what I had learned. But eventually the Radio Shack at the local mall started selling the [TRS-80](http://en.wikipedia.org/wiki/TRS-80), and I could walk into that store and write my very first program:

    10 PRINT "TRS-80 SUCKS! ";
    20 GOTO 10
    RUN

With great power comes great responsibility.

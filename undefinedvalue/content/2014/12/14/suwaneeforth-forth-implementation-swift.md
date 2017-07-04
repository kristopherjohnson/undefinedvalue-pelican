Title: SuwaneeForth: A Forth Implementation in Swift
Date: 2014-12-14 15:43:13
Category: Blog
Slug: suwaneeforth-forth-implementation-swift
Alias: 2014/12/14/suwaneeforth-forth-implementation-swift/
Tags: swift, suwaneeforth, forth


Using a new high-level programming language to implement an old low-level language is a strange thing to do, but I've done just that. _SuwaneeForth_ is an implementation of [Forth](http://en.wikipedia.org/wiki/Forth_(programming_language)) interpreter, written in [Swift](https://developer.apple.com/swift/). If you are interested in such a thing, you can find it here:

- https://github.com/kristopherjohnson/suwaneeforth

SuwaneeForth is a translation/port of the system described in "A sometimes minimal FORTH compiler and tutorial for Linux/i386 systems" (a.k.a. "[JONESFORTH](http://rwmj.wordpress.com/2010/08/07/jonesforth-git-repository/)") by Richard W.M. Jones. I'd suggest that all programmers read the source to that, as it is a very readable tutorial for bootstrapping a programming language implementation.

- [jonesforth.S](http://git.annexia.org/?p=jonesforth.git;a=blob_plain;f=jonesforth.S;hb=HEAD)
- [jonesforth.f](http://git.annexia.org/?p=jonesforth.git;a=blob_plain;f=jonesforth.f;hb=HEAD)

I heartily agree with the first paragraph of `jonesforth.S`:

> FORTH is one of those alien languages which most working programmers regard in the same way as Haskell, LISP, and so on.  Something so strange that they'd rather any thoughts of it just go away so they can get on with writing this paying code.  But that's wrong and if you care at all about programming then you should at least understand all these languages, even if you will never use them.

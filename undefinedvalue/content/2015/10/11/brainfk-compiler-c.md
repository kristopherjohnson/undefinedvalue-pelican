Title: A Brainf__k compiler in C++
Date: 2015-10-11 14:41:53
Category: Blog
Slug: brainfk-compiler-c
Alias: 2015/10/11/brainfk-compiler-c/
Tags: brainfuck


For fun, I wrote an interpreter for [a programming language with a rude name](https://en.wikipedia.org/wiki/Brainfuck), in C++.

It's available here: <https://gist.github.com/kristopherjohnson/e5fc3d19c251dc561f62>

There are other C++ interpreters for this language, but most of them look a lot more like C than like C++. My goal was to avoid archaic C-isms like pointers, fixed-size arrays, global variables, and the use of C stdio and UNIX functions, and write something that looks like "modern C++" (which may be an oxymoron). 

C++ beginners may prefer to look at the code for a simplified implementation that represents my first pass at the problem. That is available here: <https://gist.github.com/kristopherjohnson/55092ba62e82c2166125>

A collection of BF example programs is available here: <http://esoteric.sange.fi/brainfuck/bf-source/prog/>. It pleases me that the ones I've tried all work with my interpreter. The [hanoi.bf](http://esoteric.sange.fi/brainfuck/bf-source/prog/hanoi.bf) program is especially impressive.

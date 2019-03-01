Title: TSCP Translated to Rust
Slug: tscp-translated-to-rust
Date: 2019-02-28 19:25:45.962361
Category: Blog
Tags: chess, rust, tscp

A couple of years ago, I wrote [My First Chess Program](my-first-chess-program.html).  I wrote it in [Swift](https://swift.org).  It was slow, due more to my lack of knowledge rather than due to any problems with Swift.  While I was writing it, I decided not to study any other chess programs, but I did actually sneak a peak at some code in [Tom Kerrigan's Simple Chess Program](http://www.tckerrigan.com/Chess/TSCP/) (TSCP) to get an idea of what a better chess program might look like.  At the time, I meant to eventually go back and study TSCP and incorporate its good ideas into my Swift chess engine.

But that was a couple of years ago.  I'm not interested in Swift anymore (Swift is fine; it just doesn't interest me), but I have been learning [Rust](https://www.rust-lang.org), and I thought translating TSCP's [C](https://en.wikipedia.org/wiki/C_(programming_language)) code to Rust would be a way to both learn more about Rust and to study how a better chess engine works.

The result is available here: <https://github.com/kristopherjohnson/tscp-rust>.  Tom Kerrigan has given me permission to distribute my translation, but note that he still holds the copyright, and any additional redistribution is under his terms.

A lot of Rust's syntax is inspired by C, so the guts of the program look very similar.  I decided early to do as straightforward a translation as I could, without any re-design or changes to make it more "Rust-like".  However, I also wanted to minimize the amount of `unsafe` code (in the Rust sense), so I did tinker with a couple of data structures, and moved the global variables into a `struct` that gets passed between functions.

During development, I added a lot of trace output to both the C and Rust code, so I could verify that the Rust code was evaluating identical positions and getting identical results at all stages of thinking about the next move.  I found several transcription errors that I might not have found through simple testing, because the incorrect Rust program "worked" in the sense that it made valid moves, but it picked different moves to be best

The result has pretty good performance.  The `bench` command for the Rust version runs in about 580 ms, whereas the same command in the C version runs in about 520 ms.  I could probably improve the Rust performance, but I'm happy that it's in the same ballpark.  

Embarrassing story: When I first contacted Tom Kerrigan about my Rust translation, I told him that the Rust version surprisingly ran a lot faster than the C version.  He didn't believe me, but I was _sure_ that I had built the C version with all optimizations enabled, and theorized that Rust's memory safety guarantees had somehow enabled optimizations that weren't available to a C compiler.  It turned out that while the C Makefile did specify the `-O3` option for the compiler, the rule wasn't actually being applied when building the program.  So when I fixed the Makefile so that the rule worked, the C code was faster, as expected.  The good news there is that I was able to contribute the fixed Makefile back to the main TSCP codebase.

With the program translated to Rust, there are a few exercises that I want to try to explore Rust's concurrency mechanisms.  My first goal is to get it to think ahead while the opponent thinks about their move (known as "pondering" in chess-programming circles).  My next goal is to implement multicore parallel search using [ideas on Tom Kerrigan's web site](http://www.tckerrigan.com/Chess/Parallel_Search/).

My thanks to Tom Kerrigan for this cool toy.


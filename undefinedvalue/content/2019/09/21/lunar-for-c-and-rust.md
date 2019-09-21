Title: LUNAR for C and Rust
Slug: lunar-for-c-and-rust
Date: 2019-09-21 10:23:54.788026
Category: Blog
Tags: lunar, c, rust

I've written before that my first exposure to computers was a simple text-based
"[Lunar Lander](lunar-lander.html)" game.

Earlier this year I did some research
and I found the
[original LUNAR source code](http://www.cs.brandeis.edu/~storer/LunarLander/LunarLander/LunarLanderListing.jpg),
which is in the
[FOCAL](https://en.wikipedia.org/wiki/FOCAL_(programming_language))
programming language, and some
[translations to BASIC](https://www.atariarchives.org/basicgames/showpage.php?page=106).

I decided I needed to port this to a modern programming language like
[C](https://en.wikipedia.org/wiki/C_(programming_language)).

(Yes, that's intended ironically.)

The result is "LUNAR for C", which you can find on GitHub:
[kristopherjohnson/lunar-c](https://github.com/kristopherjohnson/lunar-c).

I also decided to port it to [Rust](https://www.rust-lang.org), which I was
exploring at the time. Porting to Rust was not straightforward, because the
original source code has [goto-based](https://en.wikipedia.org/wiki/Goto)
control flow, and Rust doesn't have a `goto` statement.  One way to deal with
this is to implement a simple
[state machine](https://en.wikipedia.org/wiki/Finite-state_machine) in Rust, and
the result of that experiment is available in a Gist:
[lunar.rs](https://gist.github.com/kristopherjohnson/83c6a6b8a1b7c6929ced83e922abccc1).
But I also planned to do some machine-learning experiments to find the ideal
solution to the lunar-landing problem, so I created a very over-engineered
"LUNAR for Rust" version that is available on GitHub:
[kristopherjohnson/lunar-rust](https://github.com/kristopherjohnson/lunar-rust).

If you want to play the game yourself, and you have a C compiler, I recommend
building the C version.

Thank you to Jim Storer (the original author of LUNAR), to David H. Ahl (author
of the BASIC ports), and to every other programmer who has created a
lunar-landing game that I've played.

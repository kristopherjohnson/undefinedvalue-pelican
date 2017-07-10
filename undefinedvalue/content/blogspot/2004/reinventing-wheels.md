Title: Reinventing Wheels
Date: 2004-01-23 14:16
Author: Kristopher Johnson
Tags: programming
Slug: reinventing-wheels

I have a sudden need for a store-and-forward mechanism for a C++
application I'm working on. I'm sure countless others have done this,
and there is probably an off-the-shelf solution somewhere I could use,
but I have decided to implement one from scratch.

I did spend some time on Google trying to find something that would suit
my needs, but none of the hits gave me a good feeling that I would
actually save any time or effort by using an off-the-shelf product. I
have to have this feature implemented in a couple of days, or the world
is going to end (or so customer believes), so I don't have a lot of time
to figure out someone else's product, and I definitely don't have time
to wait for a bug fix. So I've satisfied myself that I am not
reinventing the wheel without good reason.

The buy-vs.-build question is one that comes up often, and I am never
satisfied with my decision. I was once strongly in favor of "buy", but
after being stung by many low-quality products over the years, I now
tend to believe I can usually do better by myself.

The best thing about doing it myself is that the solution will be
specifically designed for my use. I don't have to learn how to manage
all the various configuration parameters that a generic off-the-shelf
"solution" would have. I don't have to worry about whether it will be
compatible with my compiler, my OS, and the other libraries I am using.
I don't have to figure out whether it is thread-safe, or how it manages
memory, or how to properly initialize and terminate it.

And of course, doing it myself is a lot more fun.


Title: Stick with the Defaults
Date: 2004-01-31 05:42
Author: Kristopher Johnson
Tags: rant, programming
Slug: stick-with-the-defaults

"It crashes in the call to bpGetStatus()."

"Do you have structure-packing set to 1?"

"Uh, no. Let me try that..."

*Five minutes later:*

"OK, now it crashes the output routine."

"Are you using the standard library?"

"Yes. Why?"

"You need to use the Gee-Cool-Whizzy port of the STL. I'll e-mail you
the URL."

"OK, I'll try that..."

Don't do this to people. The default settings for many compilers and
IDEs are perfectly reasonable. If you are going to use some bizarre
settings, write up a document or something to explain what other have to
do (and explain *why* while you're at it). The rest of us will
appreciate it.

But even better, don't use bizarre settings. I've never understood why
some people go to such lengths to find what they consider to be the
perfect set of compiler flags for their particular application. If
proper operation of the program depends upon some strange set of
compiler options, then it is almost certain that the programmer is doing
something (a) non-standard, (b) tricky, (c) incompatible with other
people's code, and (d) that is going to break when moved to another
platform or another compiler. If proper operation doesn't depend on a
strange set of compiler options, then why use them at all?

There are exceptions to this rule. For example, Visual C++'s default
settings are to statically link to a single-threaded version of the C++
runtime. For real work, almost everyone uses dynamic linking to the
multithreaded DLL. But this is not really an exception: if *everyone*
uses the same non-default setting, then you can consider it to be a
standard.

Whenever you are doing something that nobody else does, and which makes
life more difficult for everyone else, you really need to ask yourself
whether you are doing the right thing. Usually, the answer will be *No*.
Sometimes following the herd is best for everyone.


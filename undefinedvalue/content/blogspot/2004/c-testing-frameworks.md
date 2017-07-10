Title: C++ Testing Frameworks
Date: 2004-01-25 14:14
Author: Kristopher Johnson
Tags: cplusplus
Slug: c-testing-frameworks

I've always rolled my own unit-testing frameworks for C++. I don't like
CppUnit, because it is too Java-like and not C++-like. It has always
been easier to throw together what I need than to try to figure out
someone else's framework. I can throw together the basics in ten
minutes, and then evolve the test rig as necessary.

So I'm not really sure why I decided to re-examine off-the-shelf
frameworks for my current testing needs. I guess it comes down to a
desire to learn something new, and to make sure nobody else is doing
something smarter than I am.

After looking around, I settled on the [Boost Test Library](http://www.boost.org/libs/test/doc/index.htm). What I like most
about this library is that it can be used by simply \#include-ing a
header file; there is no need to build a library and link to it. The
Boost Test Library worked out-of-the-box. The only special thing I did
was to use a [debug output stream](http://www.codeproject.com/debug/debugout.asp) so that the
output shows up in the Visual C++ output window. The output format makes
it possible to double-click a line in the output window and VC++ will
open the source file and go to the source line. There is no need for a
TestRunner-style GUI.

I also ran across Michael Feathers's [CppUnitLite](http://c2.com/cgi/wiki?CppUnitLite). He created this as a
reaction to the bloat of CppUnit. CppUnitLite is intended to be just a
simple example of a testing framework, which should be modified and
extended as necessary by its users. While I like the idea of using a
simple barebones framework and modifying it as needed, CppUnitLite still
seems too complex to me.

I think that C++ unit testing is one of those things where an
off-the-shelf framework never seems right. I've come to believe that
small off-the-shelf frameworks are a bad idea. The smaller the
framework, the less it does for you and the easier it would be to roll
your own that does the job better. Only really big frameworks (MFC,
etc.) provide enough value to justify spending the time to learn them.
C++ unit testing is just too easy to justify learning a framework.

But I'll keep using the Boost Test Library for now. I hope I'll learn
something in the process. Using an off-the-shelf library might help me
to "test-infect" my co-workers.


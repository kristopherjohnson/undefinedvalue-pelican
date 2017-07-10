Title: Why Bother with .NET?
Date: 2004-01-07 14:39
Author: Kristopher Johnson
Tags: dotnet 
Slug: why-bother-with-net

Someone asked me "What's the big deal about .NET? Besides the fact that
the Microsoft world is steering that way and so knowing it is probably a
good career move. Is there a specific problem that it solves that I
couldn't solve as easily with, say, Ruby or Perl?"

This is a question I asked myself a lot while [studying for the MCSD
exams](http://kristopherjohnson.blogspot.com/2004_01_01_kristopherjohnson_archive.html#107336832099080752).
The conclusion I came to was that the primary value of .NET is that it
provides a better way to write Windows programs than C++ or Visual
Basic.

Over the years, I've learned that the best thing to do when developing
for Windows is to do it Microsoft's way. Third-party libraries and
development tools always end up "breaking" at some point because
Microsoft changes an API or doesn't provide sufficient information to
other vendors. When using non-Microsoft tools, it always seems like I
spend more time working around incompatibilities than getting my job
done. So I try to stick with Visual C++, MFC, COM, ODBC, etc., and
nobody gets hurt too badly.

So, now Microsoft provides a Java-like development platform, and is
going to be integrating it more tightly with the OS as Longhorn comes
together. What I've read in the Microsofties' blogs leads me to think
that things are generally going in the right direction. This is good in
that C++ is no longer the best way to write Windows software. Knowing
.NET lets me write better Windows software.

But aside from its ties to Windows, is .NET "better" than alternatives?
No. It has some very nice features, but I'd rather be using Python (or
Ruby, or Scheme, or Squeak, or ...).

It's not that those other things are "better" than .NET. A lot of people
knock .NET because it is not innovative, and that it is just a
collection of features that have been better implemented elsewhere. I
actually find the non-innovativeness of .NET to be comforting. The fact
that Microsoft is "stealing" a lot of good ideas from other places and
isn't trying anything too radical suggests to me that .NET is going to
be a pretty usable framework. I don't want innovation; I want something
that works.

The big drawback to .NET is that it will always be a Microsoft-specific
technology. Despite the efforts of open-source developers, I don't think
there will ever be an industrial-strength non-Microsoft implementation.
I'm not going to be able to run my .NET code on Linux, or Solaris, or
QNX Neutrino, or Palm OS, or another of the other operating systems I
develop software for.

Is it worthwhile to learn about .NET? If you develop Windows
applications, then I would definitely recommend it. If you don't develop
Windows apps, then you may want to study .NET to see how the approached
issues differently from other platforms' designers. But I can't find
anything in .NET that makes me say "Wow! This is exactly what I've been
waiting for!"


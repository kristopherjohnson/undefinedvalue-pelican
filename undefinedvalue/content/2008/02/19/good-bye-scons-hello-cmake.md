Title: Good-bye SCons, Hello CMake
Date: 2008-02-20 03:34:00
Category: Blog
Slug: good-bye-scons-hello-cmake
Alias: 2008/02/19/good-bye-scons-hello-cmake/
Tags: scons, cmake, programming


<p>
Last year, I wrote of my <a href="http://kristopherjohnson.blogspot.com/2007/03/scons.html">initial impressions</a> of <a href="http://www.scons.org/">SCons</a> for controlling software builds.  My initial impressions were positive, but even then I was wary of performance issues.
</p>
<p>
A few months later, I wrote about <a href="http://kristopherjohnson.blogspot.com/2007/07/improving-scons-performance-for-msvc8.html">a performance problem with SCons and MSVC</a>.  I was able to hack SCons to make things a little better.
</p>
<p>
Things weren't bad for me, because I've been doing all my development on Linux, where SCons is pretty well-behaved.  But the Windows developers hated it.  SCons will build MSVC project files so that developers can edit and browse code through the IDE, but the builds are still controlled by SCons, and SCons was painfully slow on Windows.  As the codebase grew, SCons got slower and slower.
</p>
<p>
The boss put up with it for a while, but he finally decided that enough was enough.  I was ordered to find something better than SCons for our cross-platform builds.
</p>
<p>
We weren't the only people dissatisfied with SCons.  The KDE team had tried SCons, found it lacking, then started their own Python-based build system based on SCons, which eventually became <a href="http://code.google.com/p/waf/">Waf</a>.  I looked at Waf briefly, but the immaturity of the project and lack of documentation turned me off.
</p>
<p>
I read that the <a href="http://en.wikipedia.org/wiki/GNU_build_system">autotools</a> system was starting to provide better support for Windows, but I didn't think that solution would go over well with the team members and leaders who passionately hate things that are too UNIX-ish.
</p>
<p>
So, after reading that the KDE team finally settled on <a href="http://www.cmake.org">CMake</a>, I decided to give that a try.
</p>
<p>
I've spent the last couple of days translating build scripts from SCons into CMake.  So far, I'm pretty pleased with the results.
</p>
<p>
<b>Pros of CMake over SCons:</b>
</p>
<ul>
<li>It generates real honest-to-goodness MSVC solution and project files that work as well as or better than those that Windows developers would create by hand.  The CMake developers don't treat Windows developers as second-class citizens.</li>
<li>The default compiler settings in the generated MSVC files and Makefiles are remarkably sane.</li>
<li>It has lots of functionality built in.  (In contrast, SCons often required lots of code to be written to do simple things.)</li>
<li>It provides a simple mechanism for handling unit tests.</li>
<li>Simpler support for hierarchical builds.</li>
<li>It has the feel of something that has been used for real-world work. (In contrast,  SCons always felt like a grad student's summer project.)</li>
<li>I don't have to go take a coffee break every time I need to do a build.</li>
</ul>
<p>
<b>Cons:</b>
</p>
<ul>
<li>I don't like CMake's syntax.  It's like they took the syntaxes of Make, Perl, Bourne shell, and BASIC, and mixed them all together.  (Please, people, stop inventing your own application-specific scripting languages!  Especially if you are going to invent one that sucks.)</li>
<li>Online documentation is poor.  You have to buy a $50 book if you want to figure things out in a reasonable amount of time.</li>
<li>While it is cross-platform, you still have to write a lot of "IF( WINDOWS ) ... ELSE ..." code.</li>
<li>It has no built-in support for precompiled headers.  (But then again, neither did SCons.  As with SCons, you can use precompiled headers by writing some code.).</li>
</ul>
<p>
I'm happy with the switch to CMake, and I'm sure the boss will be too.  But who knows; maybe next year I'll be writing yet another blog entry about the need to adopt a new build system.
</p>

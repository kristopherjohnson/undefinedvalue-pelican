Title: PowerShell and Unicode
Date: 2010-07-21 12:01:58
Category: Blog
Slug: powershell-and-unicode
Alias: 2010/07/21/powershell-and-unicode/
Tags: windows, unicode, powershell


After being away from the Windows developer world for a few years, I have been pleased to find some of the nice things that Microsoft has given us. Visual Studio has some really nice refactoring capabilities. The Windows 7 user experience rivals OS X. And as an alternative to the venerable `cmd.exe`, we now have a much better command-line shell: [PowerShell](http://en.wikipedia.org/wiki/Windows_PowerShell).

What I like most about PowerShell is that it feels more like a UNIX shell. It supports a lot of UNIXy commands (`ls`, `echo`, `cat`). It lets you use either forward slashes or backslashes in paths This is good for someone like me who can never remember what OS I'm using when I start typing a command.

But of course, Microsoft can't give us something new without throwing in some surprisingly inappropriate behavior.
<!--break-->
A couple of days ago, I needed to create a patch for a Subversion repository, and so I typed the typical command to do so (which works fine in UNIX shells and with `cmd.exe`):

    svn diff > my_patch.diff

I then looked at my patch to verify that it looked good:

    cat my_patch.diff | more

Everything looked fine. However, when I later tried to apply the patch to another Subversion workspace:

    patch -p0 -i my_patch.diff

I got errors. I opened up `my_patch.diff` in Vim, and realized it was a UTF-16-encoded file.

Neither `svn` nor `patch` know how to deal with Unicode. How did this happen?

After wasting an hour trying various `svn` command-line options and diff utilities, I finally stumbled onto the answer. It turns out that, in PowerShell, `svn diff > my_patch.diff` is equivalent to this command:

    svn diff | out-file my_patch.diff

and (get this), the `out-file` cmdlet **encodes its output as UTF-16 by default**, regardless of what the input encoding was.

This default behavior makes sense for `out-file`, but it is counter-intuitive that the `>` redirection operator would take ASCII and convert it to Unicode.

To make PowerShell do the right thing, you have to do this:

    svn diff | out-file -encoding ascii my_patch.diff

Grrr.

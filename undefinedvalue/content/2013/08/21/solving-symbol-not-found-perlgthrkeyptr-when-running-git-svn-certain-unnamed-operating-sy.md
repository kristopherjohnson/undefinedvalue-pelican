Title: Solving "Symbol not found: _Perl_Gthr_key_ptr" When Running git-svn on Certain Unnamed Operating System Beta Versions
Date: 2013-08-21 16:32:29
Category: Blog
Slug: solving-symbol-not-found-perlgthrkeyptr-when-running-git-svn-certain-unnamed-operating-sy
Alias: 2013/08/21/solving-symbol-not-found-perlgthrkeyptr-when-running-git-svn-certain-unnamed-operating-sy/
Tags: perl, osx, git, dyld, bashrc


Let's say that you are using a beta version of a new operating system that you can't name because it is covered by a non-disclosure agreement, and you have also installed the newest version of its development tools, which are also covered by NDA, and when you try to run the `git svn` command, you get this output:

    dyld: lazy symbol binding failed: Symbol not found: _Perl_Gthr_key_ptr
      Referenced from: /usr/../Library/Perl/5.12/darwin-thread-multi-2level/auto/SVN/_Core/_Core.bundle
      Expected in: flat namespace
    
    dyld: Symbol not found: _Perl_Gthr_key_ptr
      Referenced from: /usr/../Library/Perl/5.12/darwin-thread-multi-2level/auto/SVN/_Core/_Core.bundle
      Expected in: flat namespace
    
    error: git-svn died of signal 5

Apparently, the problem is that `git-svn` is implemented in Perl, and there is something wrong with the Perl configuration used when you run `/usr/bin/git`.

What do you do?

It turns out you can fix this by putting the Git executables provided by the new development tools at the head of your PATH, by executing this command (or adding it to `.bashrc`):

    export PATH="/Applications/XXXXX.app/Contents/Developer/usr/libexec/git-core":$PATH

where `XXXXX.app` is the unnamed development tool.

Alternatively, you can add all the command-line tools to your PATH like this:

    export PATH=”/Applications/XXXXX.app/Contents/Developer/usr/bin/”:$PATH

Credit to [Vandad Nahavandipoor](http://vandadnp.wordpress.com/2012/04/06/git-from-command-line-after-installing-xcode-on-os-x-lion/) for the hint.

Another option would be to use the [xcrun](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/xcrun.1.html) utility to run `git`. You can do this:

    xcrun git svn blah-blah-blah

or put this into your `.bashrc` so that you don't have to remember to type `xcrun`:

    alias git='xcrun git'

If you are the kind of person who thinks its a good idea to replace system files with symlinks, you might try symlinking `/usr/bin/git` to `/Applications/XXXXX.app/Contents/Developer/usr/libexec/git-core/git`. However, that alone doesn't work, because Git will still run the `git-svn` executable from its default location, `/Library/Developer/CommandLineTools/usr/libexec/git-core`, and you will still have the `_Perl_Gthr_key_ptr` problem. So you also need to symlink the default location to `/Applications/XXXXX.app/Contents/Developer/usr/libexec/git-core/`, or set the `GIT_EXEC_PATH` environment variable.

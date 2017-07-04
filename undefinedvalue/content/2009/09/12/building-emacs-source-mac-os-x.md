Title: Building Emacs from Source for Mac OS X
Date: 2009-09-12 22:29:05
Category: Blog
Slug: building-emacs-source-mac-os-x
Alias: 2009/09/12/building-emacs-source-mac-os-x/
Tags: osx, mac, emacs


There are a few binary Emacs packages for OS X floating around out there, but I always build it myself from the sources. This usually results in an Emacs that works the way I expect, rather than the way some "helpful" distributor thinks it ought to work.

I'll assume you have the developer tools and `bzr` installed, and know how to open Terminal and type some commands. Here are the commands you need to type:

> bzr init-repo --2a emacs/
>
> cd emacs
> 
> bzr branch bzr://bzr.savannah.gnu.org/emacs/trunk/
> 
> cd trunk
>
> ./configure --with-ns
> 
> make install

When this is complete, you'll end up with `Emacs.app` in the `nextstep` subdirectory. You can run `Emacs.app` from there, or copy it to your Applications directory.

----

**Update 2010/10/29:** Discovered that the Emacs team now uses Bazaar (`bzr`) rather than CVS. Updated the instructions accordingly, following advice from http://www.emacswiki.org/emacs/EmacsForMacOS and http://www.emacswiki.org/emacs/BzrForEmacsDevs. Also, found what appears to be a faithful binary distribution at http://emacsformacosx.com/.

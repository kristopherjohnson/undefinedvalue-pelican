Title: Emacs for OS X
Date: 2004-10-13 22:58
Author: Kristopher Johnson
Tags: mac, emacs
Slug: emacs-for-os-x

One of the first things I wanted for my Mac was a good text editor.
TextEdit is okay for simple tasks, and I can use vi in a pinch, but I
really wanted something like Emacs.

So I started searching for Emacs/XEmacs for OS X. I found about a dozen
different builds from different sources. Some ran on X11, some ran only
in the Terminal. Some were relatively new (Emacs 21); some were pretty
old (Emacs 19).

The best one I found is a Japanese-built [Carbon Emacs
Package](http://home.att.ne.jp/alpha/z123/emacs-mac-e.html). This one is
built from the current sources in the Emacs CVS repository, and doesn't
require an X11 server.

One problem with this version is that font support is bad. The default
font is a big Monaco font. I tried changing font faces, but always ended
up with something worse than the default (which is ugly). This package
is apparently designed for Japanese users, and the Roman font support
just isn't there. Every attempt to use the Set Font/Fontset command
results in a "Font not found" error, and attempts to use the
Customization screens result in something uglier than the default. I
decided that I can live with the default font.

There are some non-Japanese builds of Emacs with Carbon floating around,
so I'll give those a try. Eventually, I'll overcome my natural laziness
and figure out how to build it myself.

By default, the Command key is used as the Emacs Meta key. I prefer
using the Alt/Option key, so I added this to my .emacs file:

      (setq mac-command-key-is-meta nil)


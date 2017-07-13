Title: Screwed by FileMerge
Date: 2004-10-30 06:48
Author: Kristopher Johnson
Tags: menubarcountdown, versioncontrol, filemerge
Slug: screwed-by-filemerge

While adding support for stored preferences to Rouser, I realized I
needed to add another outlet to my controller class so that it could
restore the setting of the on/off radio buttons. So I went into
Interface Builder, added the outlet, and told it to regenerate the class
files. When prompted, I clicked the "Merge" button to indicate that I
wanted the new code merged into the existing files, instead of
overwriting the files.

The FileMerge application started, and the windows opened. As I've done
before, I just looked for "0 conflicts" and then did a Save of the
files. (I ignore all the shaded curvy lines and arrows on the FileMerge
display, because I don't understand what they mean.)

BZZZT! It didn't merge. It just overwrote my class files with a bunch of
empty declarations. Intuitive, forgiving interface, hah!

I commit to CVS pretty often, so this wasn't a disaster. I suppose I
really ought to read the docs for FileMerge one of these days. But why
doesn't this do the right thing by default? You know, like a Macintosh
would.


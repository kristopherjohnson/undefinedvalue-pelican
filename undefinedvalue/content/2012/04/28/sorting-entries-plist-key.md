Title: Sorting Entries in a PList by Key
Date: 2012-04-28 16:22:11
Category: Blog
Slug: sorting-entries-plist-key
Alias: 2012/04/28/sorting-entries-plist-key/
Tags: python, plist


My iOS applications use [property list](http://en.wikipedia.org/wiki/Property_list) (plist) files to specify configuration parameters and other stuff. I was trying to do some comparison and merging of these plists, but was tripped up because the keys were in different order in different files.

So I whipped up a little Python script to sort the keys in the plists and write them in a canonical format. If you would be interested in such a thing, it's as easy as this:

<script src="https://gist.github.com/2519997.js?file=sortplist.py"></script>

Title: UTF-8
Date: 2011-04-06 14:48:23
Category: Blog
Slug: utf-8
Alias: 2011/04/06/utf-8/
Tags: unicode, rant


Matt Gallagher's ["User interface strings in Cocoa"](http://cocoawithlove.com/2011/04/user-interface-strings-in-cocoa.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+CocoaWithLove+%28Cocoa+with+Love%29) post is good for its overall purpose (telling people how to use `NSLocalizedString()`), but I especially like this little embedded rant:

> **A quick swipe at almost everybody:** UTF-8 has been around since 1993 and Unicode 2.0 since 1996; if you have created any 8-bit character content since 1996 in anything other than UTF-8, then I hate you.<br><br>I weep to think of the years of programmer time that are still wasted attempting to support non-Unicode formats without characters getting garbled because people are still creating content using ancient encodings without useful identifiers to indicate what nonsense encoding they're using (or worse, people creating content that explicitly uses the wrong encoding for an encoding-specific text field).<br><br>MacRoman? Atrocious. Big-5? I hope you want to see garbage output. Windows Latin? You suck. If you're creating new content using anything other than UTF-8, UTF-16 or UTF-32 then you should be forced to serve prison time with whatever idiot monkey decided that UTF-16 should be allowed little-endian and big-endian variants instead of a single authoritative encoding.

Yeah, seriously. If you call yourself a programmer, but you don't understand what all this Unicode, UTF-8, and UTF-16 business is about, please read Joel Spolsky's [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](http://www.joelonsoftware.com/articles/Unicode.html).


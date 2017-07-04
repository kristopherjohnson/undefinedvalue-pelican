Title: HTML Man pages
Date: 2012-06-25 02:31:25
Category: Blog
Slug: html-man-pages
Alias: 2012/06/24/html-man-pages/


If you've used UNIX-based systems, you're probably aware of [man pages](http://en.wikipedia.org/wiki/Man_page). And you know that they suck.

To make them a little less sucky, I wrote a little shell script called `hman` which displays a man page as HTML in the browser, rather than forcing you to use `less`. Here it is, if you'd like such a thing. (You'll need to install `man2html` via [Homebrew](http://mxcl.github.com/homebrew/)).

<script src="https://gist.github.com/2983879.js"> </script>

So, with this, you can run `hman bash` and get something halfway usable.

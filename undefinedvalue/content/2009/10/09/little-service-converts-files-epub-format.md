Title: A Little Service That Converts Files to EPUB Format
Date: 2009-10-09 13:26:19
Category: Blog
Slug: little-service-converts-files-epub-format
Alias: 2009/10/09/little-service-converts-files-epub-format/
Tags: service, reader, osx, mac, epub, automator, sonyreader


<!--break-->
My wife recently gave me a nice gift: a [Sony Reader](http://en.wikipedia.org/wiki/Sony_Reader) device. She'd been watching me read books using the Kindle for iPhone app, and felt sorry for me because I had to read from such a small screen. The Reader is really nice. (Thanks, honey.)

Now I'm learning all about how to get content onto the device. The Sony&nbsp;eBookLibrary software that you use to copy files to the device is pretty bad (worse than iTunes, if you can believe that), so I'm using it as little as possible. I ran across [calibre](http://calibre.kovidgoyal.net/), a nice open-source tool for managing various e-reader devices. Unfortunately, it can't handle the DRM'ed files that one downloads from the Sony&nbsp;eBookstore, and after transferring books to the device, the device often crashes and has to reboot itself.

So, my compromise for now is to use calibre's `ebook-convert` command-line utility to convert files to EPUB format, and then use Sony eBookLibrary to transfer those to the device. To make this easier, I've created a service, using Automator, that will invoke `ebook-convert` on files selected in the Finder.

If you want such a thing for yourself, here's how to make it:

## Install the calibre command-line tools

0. Download [calibre](http://calibre.kovidgoyal.net/download) and install it.
0. Start calibre, and click the **Preferences** toolbar button.
0. Select Advanced in the list on the left, and click the **Install command-line tools** button.

## Create the service

(Note: This requires Mac OS X 10.6 Snow Leopard or newer.)

0. Start the Automator application.
0. When prompted to choose a workflow template, select **Service** and click **Choose**.
0. In the **Service receives selected** list, choose **documents**.
0. In the **in** list, choose **Finder**.
0. Drag a **Run shell script** action from the list into the workflow area.
0. Leave the **Shell:** option set to **/bin/bash**
0. For the **Pass input:** option, choose **as arguments**
0. Change the script text to this:
<pre>
    for f in "$@"
    do
        /usr/bin/ebook-convert "$f" "$f.epub" --output-profile=sony
    done
</pre>
0. Choose the **File -> Save** menu item, and give the service a name like "Convert to EPUB"

To test your new service, go to the Finder and select a text, RTF, PDF, or other such file, and then choose the **File -> Services -> Convert to EPUB** menu item. Note that conversion may take a while, depending upon how large the input file is.

I am a newbie at this. If there are better ways, I'd love to hear about them.

Title: My First AppleScripts
Date: 2004-11-11 06:07
Author: Kristopher Johnson
Tags: applescript
Slug: my-first-applescripts

OK, they aren't really my first AppleScripts. I used AppleScript a lot
back in the Mac OS 7 days, but unfortunately most of the applications I
used back then didn't support it very well. I was hoping things would be
better now, but they really aren't. Apple's applications have reasonable
support, but many third parties' applications do not.

Case in point: Mozilla Firefox 1.0. Released this week, I read several
Mac users' comments that we finally have a good browser for Mac OS. On
Windows, I prefer Firefox to IE, but on Mac, it is not as good as
OmniWeb, and is not better than Safari. What really bugs me about
Firefox is the lack of support for basic Mac features, especially
AppleScript.

But anyway, I found a need for a simple AppleScript today. I use
[Shrook](http://www.shrook.com) as my RSS reader. Shrook is nice, but is
still not very polished. I was trying to download Adam Curry's [Daily Source Code](http://www.dailysourcecode.com) MP3 from the Shrook window,
but the "Download Linked File" item on the context menu had no effect.
So I opened the page in OmniWeb, but OmniWeb wanted to download the
whole file and then play it in an ugly embedded QuickTime viewer. What I
really wanted to do was get iTunes to stream it, but didn't want to go
through all the hoo-hah of opening the URL in iTunes.

I haven't used AppleScript for years, so I spent a long while looking at
various examples on the web and experimenting with different concepts. I
finally came up with a script that would let me copy the MP3 URL to the
clipboard, and then select "Open Clipboard Location in iTunes" from my
Script Menu. Here's the script, which I saved as "Open Clipboard
Location in iTunes.scpt" in `~/Library/Scripts`:

    :::applescript
    tell application "iTunes"
        set theLocation to (the clipboard as text)
        open location theLocation
    end tell

Very simple, like it should be.

After that little exercise, I decided I'd like a similar script that
would open a URL from the clipboard in a new tab in OmniWeb. OmniWeb has
the richest AppleScript support of all the Mac browsers I've seen.
Here's the script:

    :::applescript
    tell application "OmniWeb"
        activate
        if (count browsers) < 1 then
            make new browser at front of browsers
        end if
        set theUrl to (the clipboard as text)
        tell front browser
            set theNewTab to (make new tab at end of tabs with properties {address:theUrl})
            set active tab to theNewTab
        end tell
    end tell


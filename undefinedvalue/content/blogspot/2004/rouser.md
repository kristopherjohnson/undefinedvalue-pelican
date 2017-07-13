Title: Rouser
Date: 2004-10-29 12:40
Author: Kristopher Johnson
Tags: menubarcountdown
Slug: rouser

My "Rouser" alarm clock application for Mac OS X is coming along nicely.
It is basically functional now, allowing me to turn the alarm on and off
and set the alarm time. When it is on, it displays a countdown (e.g.
"Alarm will ring in 2 hours, 13 minutes, 12 seconds") that updates once
per second. When the alarm goes off, it repeatedly speaks the current
time ("The time is 12:49 PM.") for a minute or until the alarm is turned
off.

I am using the "Bells" voice to speak the time. This sounds like a
grandfather clock's chimes, emphasizing the clockiness of the
application. I couldn't find anything in Apple's current documentation
about the special delimiters one can use to control the voice (for
example, "[[slnc 1000]]" to pause for a second, or "[[rate -10]]" to
slow it down), but I was able to find plenty of unofficial information
around the web. Interestingly, the most informative sites were by Newton
enthusiasts. Once I knew what to look for, I did find some info on
[embedded speech commands](http://developer.apple.com/documentation/mac/Sound/Sound-200.html)
in Apple's online *Inside Macintosh: Sound*.

There are just a few little things I want to add to Rouser before I can
call it "finished":

-   an Options panel allowing the user to change the voice, to change what it says, or to play a sound instead of a voice
-   saving the state of the alarm clock to a plist file
-   displaying an "Are you sure you want to quit?" panel if user tries to quit while the alarm is on and counting down
-   a nifty application icon that does cool things in the Dock

I currently have three pop-up menus to choose the time: the first has
the numbers 1-12, the second has the numbers 00, 05, 10, ... 55, and the
last has "AM" and "PM". This allows me to set the time fairly quickly,
without using the keyboard. If I still feel ambitious after "finishing"
the application, I'd like to implement pie-like menus for the numeric
fields.

So far, I'm pretty impressed with Interface Builder and the Cocoa API.
Everything I've wanted to do has been pretty simple to implement. If I
wasn't learning OS X programming while implementing Rouser, I think I
could have put the whole thing together in less than an hour.

The only gripe I have about Cocoa is that the date/time classes don't
seem to provide any easy way to extract the current hour, minute, and
second. So I had to fall back on the standard C `time()` and
`localtime()` functions, which aren't described in Xcode's
documentation. Apple clearly wasn't considering the needs of alarm-clock
developers - this is more undeniable evidence of Apple's irrational
anti-alarm-clock bias.


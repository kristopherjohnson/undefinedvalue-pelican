Title: Alarm Clock
Date: 2004-10-12 18:07
Author: Kristopher Johnson
Tags: mac, apple, menubarcountdown
Slug: alarm-clock

One of my favorite desk accessories on the old Mac was the Alarm Clock.
Mac OS X doesn't have one. Neither does Windows. I miss it.

I don't know why it disappeared. I guess they figure the
appointment-setting features of iCal, Outlook, or Entourage eliminate
the need for a simple alarm clock. But they don't: I often want my
computer to remind me when a TV show is coming on, or to check the oven
in ten minutes, or for other impromptu events, and I don't want to go
through the whole process of creating an appointment (specifying date,
time, length, location, who's attending, etc.).

I found a few alarm-clock utilities for OS X, but none of them do
exactly what I want, and the more useful ones are not free. So I may
need to write my own alarm clock application. This will be my chance to
learn to write a Cocoa app.

In the meantime, I'm just going to use the UNIX 'at' command from the
Terminal to trigger the speech synthesizer. I can use it like this:

    localhost:~ kdj$ at 13:50say -v Vicki 'Kris, it is time to go back to work!'^D

and then a soothing female voice will gently wake me from my afternoon
nap.

If you decide to use 'at' yourself, be sure to read the man page for at.
It is necessary to enable the 'atrun' command in /etc/crontab before it
will work.


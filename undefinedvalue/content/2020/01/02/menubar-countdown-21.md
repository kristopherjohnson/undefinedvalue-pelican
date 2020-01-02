Title: Menubar Countdown 2.1
Slug: menubar-countdown-21
Date: 2020-01-02 09:14:53.417195
Category: Blog
Tags: menubarcountdown,pomodoro,mac,software

Way back in 2009, I released [Menubar Countdown 1.0](/menubar-countdown-10-mac-os-x-released.html).  It's a simple app that displays a countdown timer in the Mac menu bar.  I created it because I was experimenting with the [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique) and I didn't like any of the other timer apps I tried.

I made a few updates in 2009, culminating with [Menubar Countdown 1.2](/menubar-countdown-12-released.html) in June.  And for a long time, that was it.  It was simple, and I liked it that way.  I'd occasionally get feature requests, but the suggested features didn't appeal to me.

Back in 2015, I did translate the code from Objective-C to Swift 2.1.  There was no reason to do this other than to get some experience using Swift.  I had a vague plan to submit it to the Mac App Store, but I just kept it to myself.  The 2009 version was still working, and nobody was complaining.

That changed in early 2019.  Menubar Countdown 1.2 is a 32-bit application, and [macOS Mojave warned](https://github.com/kristopherjohnson/MenubarCountdown/issues/2) that 32-bit applications would not be supported in the next version of macOS.

"Hmm, I should probably do something about that," I thought.  Then I forgot about it.

I was reminded in October 2019 when a user, John Cornell, emailed me to let me know he really wanted Menubar Countdown working on Catalina, so he had tried to update the code himself, but couldn't get it to work.

With a user motivated enough to try to fix it himself, I finally got off my virtual butt and made the necessary updates to get the Menubar Countdown 1.x codebase updated so that it would build with Xcode 11 and run on macOS Catalina.  I released that version as [Menubar Countdown 1.3](https://github.com/kristopherjohnson/MenubarCountdown/releases/tag/1.3).

But that wasn't enough.  With my hands in the code, I remembered all the changes I've thought about making over the past decade.  I wanted to release it through the Mac App Store.

I did those things.  The result is Menubar Countdown 2.1.  You can now download the app from the Mac App Store at <https://apps.apple.com/us/app/menubar-countdown/id1485343244?mt=12>.  If you don't like the Mac App Store, you can download a notarized build from <https://github.com/kristopherjohnson/MenubarCountdown/releases/tag/2.1>.

It's still free and open-source, with a project page at <https://github.com/kristopherjohnson/MenubarCountdown>.  I've changed the license from [LGPL](https://opensource.org/licenses/lgpl-license) to [MIT-style](https://opensource.org/licenses/MIT).

Now I hope I can ignore it for another decade.


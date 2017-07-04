Title: Menubar Countdown 1.0 for Mac OS X Released
Date: 2009-04-06 21:52:00
Category: Blog
Slug: menubar-countdown-10-mac-os-x-released
Alias: 2009/04/06/menubar-countdown-10-mac-os-x-released/
Tags: pomodoro, mac, gpl, cocoa, menubarcountdown, software


<p>Lately, I've been experimenting with the <a href="http://www.pomodorotechnique.com/">Pomodoro Technique</a> for time management.  The basic idea is that you work in focused 25-minute bursts, with short breaks between bursts.  You are supposed to use a kitchen timer to avoid getting distracted by looking at the clock.
</p>
<p>
Of course, as a computer guy I'd like my timer to be on my computer.  I looked around for a Mac application that would provide an unobtrusive 25-minute countdown timer, but I didn't find any that I liked.  So I decided to write my own.
</p>
<p>
<a href="http://capablehands.net/menubarcountdown">Menubar Countdown</a> is the result of that effort.  It displays a countdown timer on the right side of the menu bar.  It has menu items that allow you the user to start, stop, or resume the timer.
</p>
<p>
There are three options for what you want to happen when the timer reaches 00:00:00:
</p>
<ul>
<li>Play the system alert sound (which I never notice).</li>
<li>Display an alert window (which is effective, but you may not like the abrupt interruption).</li>
<li>Speak.  This is my favorite option.  You can specify what you want the application to say.</li>
</ul>
<p>
It's free software, distributed under the terms of the <a href="http://www.gnu.org/copyleft/gpl.html">GNU General Public License</a>.
</p>
<p>
Source code is included.  Other neophyte Cocoa programmers might find it useful as an example of using such classes as NSStatusBar, NSStatusItem and NSUserDefaultsController, or for measuring absolute time in a Mac application.
</p>
<p>
You can download the application from my snazzy new corporate web site: <a href="http://capablehands.net/menubarcountdown">Menubar&nbsp;Countdown product page</a>.
</p>

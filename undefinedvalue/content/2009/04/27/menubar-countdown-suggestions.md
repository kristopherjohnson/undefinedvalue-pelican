Title: Menubar Countdown Suggestions
Date: 2009-04-27 16:59:49
Category: Blog
Slug: menubar-countdown-suggestions
Alias: 2009/04/27/menubar-countdown-suggestions/
Tags: menubarcountdown


Since releasing [Menubar Countdown](http://capablehands.net/menubarcountdown), my little Mac OS X timer app, I've received some nice feedback and suggestions for improvement. I'm going to list them here, both so that I can find them later, and to let others leave their own suggestions.

- Repeat the alarm until the user acknowledges it. (Currently, the alarm just goes off once.)
- Support Growl notifications
- Allow user to choose an alert sound other than the default system alert sound.
- Provide option to log out and/or shutdown when timer expires.
- Provide option to launch an application or an AppleScript when timer expires.
- Add a _days_ field.
- Allow user to specify the output format (so that a user could, for example, have it display "4m, 3s" instead of 00:04:03.
- One-click start: bypass the Settings dialog
- Animated "alarm is going off" display
- Allow user to specify an ending date and time, rather than a time interval
- Provide option to not display seconds (continuous animation is distracting to some, and removing seconds would save some menubar real estate)

I'm not going to implement very many of these, if any. What I like about Menubar Countdown is its simplicity, both in terms of user interface and in terms of implementation. It's only a couple hundred lines of code, and I'd like to keep it that way.


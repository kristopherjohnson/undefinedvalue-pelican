Title: JacksOrBetter as a Web App
Date: 2010-01-02 14:38:01
Category: Blog
Slug: jacksorbetter-web-app
Alias: 2010/01/02/jacksorbetter-web-app/
Tags: jquery, javascript, jacksorbetter


A little over a year ago, I created my first iPhone app, [JacksOrBetter](https://undefinedvalue.com/2008/09/07/jacksorbetter-iphone-and-ipod-touch). As an exercise in learning CSS, JavaScript, and jQuery, I've created a web-based version of JacksOrBetter.

- http://jacksorbetterpoker.appspot.com/
<!--break-->
It should work on any decent web browser (that is, one that has good implementations of JavaScript and CSS2). It uses a few WebKit-specific features, so it looks a little better on Safari and Google Chrome than it does on Firefox and Internet&nbsp;Explorer. It doesn't require Flash or Java; it's just plain-old HTML, CSS, and JavaScript.

If you'd rather control it with the keyboard then by clicking buttons, you can use the space bar to deal/draw, and you can use the numeric keys 1, 2, 3, 4, and 5 to specify which cards to hold.

Implementing a jacks-or-better poker game is my standard exercise for learning a new programming language or development platform. It is simple, without being trivial. The user interface can be very simple or very complex, depending upon my mood.

While this app is basically functional now, there are still a lot of features and refinements to be added. For example, I need to show a payout table. The animations could also use improvement.

While this app works fine in a desktop browser, I'm really targeting it at the iPhone and similar platforms. Right now, it is a bit sluggish on iPhone. I'm going to start playing with [jQTouch](http://www.jqtouch.com/) to give it more of a native-app feel.

One nifty feature that does work on the iPhone is that, after initial loading from the web, it can be run while offline.

I'd be interested to hear how well it works on Android and Palm Pre. It works on the emulators, but I don't have actual devices to test. Please let me know.

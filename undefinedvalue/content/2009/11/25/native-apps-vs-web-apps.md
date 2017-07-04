Title: Native Apps vs. Web Apps
Date: 2009-11-26 00:08:18
Category: Blog
Slug: native-apps-vs-web-apps
Alias: 2009/11/25/native-apps-vs-web-apps/
Tags: webdev, iphone, android


This week, there was a lot of chatter in the blogosphere about the prospect of writing [web apps for the iPhone](http://www.apple.com/webapps/whatarewebapps.html) instead of developing native apps.
<!--break-->
The furor started with Peter-Paul Koch's profanity-laden rant entitled ["Apple is not evil. iPhone developers are stupid."](http://www.quirksmode.org/blog/archives/2009/11/apple_is_not_ev.html). In this post, PPK asserts that most iPhone applications could easily have been implemented as web applications rather than as native apps that have to be downloaded from the App Store, but iPhone developers are just too stupid to take advantage of web technologies.

PPK obviously has a chip on his shoulder over the fact that web developers are not given the same respect as "real programmers", but he did raise some good points. There are a lot of simple form-based iPhone apps that could easily have been done as web apps, thus avoiding entanglements with Apple's review process and also providing compatibility with platforms other than the iPhone.

However, PPK was also wrong on several points. He overestimated the capabilities of the iPhone's mobile browser; many of the things he thought could be done in-browser really can't be (yet). He also completely ignored two major benefits of native apps: they look nicer and developers have an easy way to get paid for making them. Cocoa developers have [many good reasons](http://farukat.es/journal/2009/11/347-iphone-developers-arent-stupid-ppk) for choosing the Cocoa Touch framework over web technologies, even in cases where a web app could compare well to a native app.

PPK has backpedaled a bit, and his follow-up posts have been a little more reasonable and balanced than the original. But other iPhone developers have jumped on the bandwagon, pointing out that maybe too many Cocoa developers really are just too lazy and arrogant to [learn enough about HTML, CSS, and JavaScript to make web apps for iPhone](http://developer.apple.com/safari/).

A healthy iPhone web-app industry would lead to interoperability with Android and other mobile platforms, and would loosen Apple's stranglehold on its platform. Unfortunately, there is no App Store for iPhone web apps, so they can be hard to find. Apple does have a [web apps page](http://www.apple.com/webapps/) with a lot of links to web apps, but most iPhone users have no idea that it exists. 

It's a bit ironic, because in the early days of the iPhone, Apple was telling developers that web apps were the way to go, and there was no need for a native SDK. At that time, most developers scoffed. Developers wanted to create high-performance games and apps that looked as nice as the built-in apps (Mail, Contacts, Google Maps, etc), and those things could not be done as web apps. And there is a lot of truth to the idea that "real programmers" look down on web development as an activity for those not smart enough to learn C, and see web apps as toys.

However, thanks to PPK's nudge, a few influential iPhone developers have started talking about web technologies. As a proof-of-concept, there is the game [Pie Guy](http://mrgan.tumblr.com/post/257187093/pie-guy) by Neven Mrgan, which is a web application but which acts a lot like a native app.

Other iPhone developers have started talking about the [Cappucino Web Framework](http://cappuccino.org/), an open-source framework that allows one to use an API that is very similar to the Mac Cocoa frameworks. In this way, Cocoa developers can write iPhone web apps without having to learn too much (an approach which I don't like, but which has some merit).

I myself have wanted to spend more time learning the ins and outs of JavaScript, CSS, and the DOM, but I've never had a "real project" that forced me to do so. Maybe it's time to find one.

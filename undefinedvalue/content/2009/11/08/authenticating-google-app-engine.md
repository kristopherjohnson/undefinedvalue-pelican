Title: Authenticating with Google App Engine
Date: 2009-11-09 01:01:56
Category: Blog
Slug: authenticating-google-app-engine
Alias: 2009/11/08/authenticating-google-app-engine/
Tags: iphone, googleappengine, cocoa


I've finally got around to doing some work on that iPhone application that I've [committed to finishing this month](https://undefinedvalue.com/2009/11/01/not-quite-nanowrimo).

On days I do a lot of work on the app, I don't feel obligated to work too hard on the blog, but I will post a little something about whatever I worked on. Today, I got my iPhone app to connect to a [Google App Engine](http://code.google.com/appengine/docs/whatisgoogleappengine.html)-based web site.

Without giving away too much, I'll just say that the iPhone app and the web site work together to provide a service to iPhone users.  I put the web site together in a couple of weekends. I decided to use Google Accounts for authentication, meaning that to log into my web site, either via a web browser or via the iPhone app, a user has to provide a Google account ID and password.

If you do things this way, the server-side authentication stuff is easy. However, writing the client side is not easy, because the mechanism for authenticating with a Google account and connecting to a Google App Engine web site is not well documented. Luckily, I found a [Stack Overflow question and answer](http://stackoverflow.com/questions/471898/google-app-engine-with-clientlogin-interface-for-objective-c) that provided all the clues I needed to get my iPhone app working.

After using Google's API for implementing the web site, I'm growing increasingly frustrated with the Cocoa APIs. What takes two lines of code on the web side takes dozens of lines of code on the client side. Simple operations like connecting to a URL, downloading data, and storing it to a local database requires a lot of boilerplate code on the Cocoa side. It's not difficult, but it's incredibly verbose.

I should note that I'm using the Python API for Google App Engine. If I was using the Java API, then I'm sure it would be as grotesque as the Objective-C stuff.



Title: Beware the Lure of the iOS UIWebView
Date: 2011-07-26 00:32:03
Category: Blog
Slug: beware-lure-ios-uiwebview
Alias: 2011/07/25/beware-lure-ios-uiwebview/
Tags: ios


Apple's iOS SDK provides a class, [UIWebView](http://developer.apple.com/library/ios/#documentation/uikit/reference/UIWebView_Class/Reference/Reference.html), that provides a simple way to display HTML content in an iOS application. Many apps use UIWebView to display web pages, online help, and other formatted content.

For the basic purpose of displaying HTML content, it works pretty well. However, as it appears to just be a wrapper around WebKit, one might be tempted to use it to try to implement a full-fledged web browser embedded in an application. _Don't do this!_ UIWebView has many limitations that make it unsuitable for this purpose:

   * Many commonly used JavaScript functions, such as `alert()` and `window.open()`, don't work at all or only work in limited ways in a UIWebView. So many of the web sites one would try to visit do not work in a UIWebView.
   * There are limited hooks for customizing the behavior. There are a few delegate methods that notify your app when the web view starts loading or finishes loading, but you can't detect many of the events you'd really want to detect.
   * UIWebView does not send the same browser identification info that Mobile Safari does, so some servers will treat it as an unknown browser and return limited content.

Of course, some intrepid developers have found ingenious ways to work around some of these limitations. If you really want to try it, or if you are curious about what kinds of hackery are needed to use UIWebView as a web browser, check out these links:

   * [WebKit on the iPhone, part 1](http://www.icab.de/blog/2009/07/27/webkit-on-the-iphone-part-1/) and [part 2](http://www.icab.de/blog/2009/08/05/webkit-on-the-iphone-part-2/)
   * [7 tips for using UIWebView](http://www.codingventures.com/2008/12/using-uiwebview-to-render-svg-files/)

The lesson I learned (after several hours of banging my head against the wall) is to pass web URLs over to Safari, rather than trying to display them in a UIWebView within my app. It's just not the right tool for this job.

----

**Update (2011/10/1):** My original post included this bullet point:

   * You can't control authentication. UIWebView can open an HTTPS connection, but if the server-side certificate is self-signed, there is no way to get it to ignore the certificate, and so it just fails with an error message.

I've been informed that this is not entirely true. It is possible to somehow "preconnect" to the server with an NSConnection, deal with authentication, and then pass the credentials to the UIWebView. More information is available here: http://stackoverflow.com/questions/11573164/uiwebview-to-view-self-signed-websites-no-private-api-not-nsurlconnection-i/15074358#15074358

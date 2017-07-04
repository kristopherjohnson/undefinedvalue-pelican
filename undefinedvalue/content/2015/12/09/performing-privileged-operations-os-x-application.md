Title: Performing Privileged Operations in an OS X Application
Date: 2015-12-10 04:16:27
Category: Blog
Slug: performing-privileged-operations-os-x-application
Alias: 2015/12/09/performing-privileged-operations-os-x-application/
Tags: osx


I am currently developing an OS X application. The application needs to perform some operations that require root privileges (installing and uninstalling launchd daemons, sending signals to other users' processes, etc.) So I started looking for some documentation about how to do that. I figured it would take a few minutes.

A day later, I finally think I understand it. The solution isn't complicated, but learning about it was difficult for a few reasons:

- Apple's "Authorization Services Programming Guide" is woefully out of date. It tells you to use `AuthorizationExecuteWithPrivileges()`, but that has been deprecated since OS X 10.7. It also has links to sample code that doesn't exist anymore. (Apple developer documentation people: It seems many of your docs are way out of date. Pls fix.)
- Apple provides a [SMJobBless](https://developer.apple.com/library/mac/samplecode/SMJobBless/Introduction/Intro.html) sample that purports to demonstrate how to use the new `SMJobBless()` API that replaces `AuthorizationExecuteWithPrivileges()`. However, while it does indeed install some kind of service that could in theory run as root, the service it installs doesn't do anything, so it is useless as an example. (But you could waste a lot of time with it before you figure that out.)
- A lot of old documentation and sample code for the original low-level XPC API is still floating around, but once you have a clue (which I didn't), you'll just use the high-level `NSXPCConnection` API.

So, in the hope I can help others avoid this tortuous path, here is how i would suggest others learn how to do this:

- Study the [EvenBetterAuthorizationSample](https://developer.apple.com/library/mac/samplecode/EvenBetterAuthorizationSample/Listings/Read_Me_About_EvenBetterAuthorizationSample_txt.html), which is up to date (as of OS X 10.11, anyway) and actually does something you can test and copy. Especially study the README file, which provides more information about `SMJobBless()` than any other Apple document.
- Watch the [WWDC 2012 Session 241 "Cocoa Interprocess Communication with XPC"](https://developer.apple.com/videos/play/wwdc2012-241/) video if you are unfamiliar with XPC.

And here is what I wish somebody could have told me before I started:

- What you will need to do is create a "helper tool" application to perform the privileged operations. This will be a command-line app that creates an XPC listener and handles requests.
- The helper app has to have an info.plist and a launchd plist with some magical keys (see the EvenBetterAuthorizationSample for details)
- The helper app will be embedded in the main app's package.
- The main app will use the `AuthorizationCreate()` and `SMJobBless()` functions to authenticate the user and install the helper tool as a privileged launchd service. (This is the point where the system will display a dialog asking the user for an admin username and password.)
- After the helper tool is installed, use `-[NSXPCConnection initWithMachServiceName:options:]` to connect to the helper tool. This will launch the helper tool on demand, running with root privileges.


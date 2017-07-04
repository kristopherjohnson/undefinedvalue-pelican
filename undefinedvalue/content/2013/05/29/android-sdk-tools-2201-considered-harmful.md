Title: Android SDK Tools 22.0.1 Considered Harmful
Date: 2013-05-29 23:43:08
Category: Blog
Slug: android-sdk-tools-2201-considered-harmful
Alias: 2013/05/29/android-sdk-tools-2201-considered-harmful/
Tags: rant, android


After finishing up some work on an iOS app today, it was time to go make equivalent changes to the Android port of that app. "I'll just update my Android SDK before I get to work," I said (to myself). I opened the Android SDK Manager and let it update these SDK packages to these versions:

- Android SDK Tools: 22.0.1
- Android SDK Platform-tools: 17
- Android SDK Build-tools: 17

Then I let Eclipse update the ADT. Then I got to work. I opened my Android app project and tried to run it. I found I couldn't make a working debug build or a release build, nor could I create a signed APK to install on a device.

After a few hours of hair pulling, I got everything working. Here is what I learned. I hope it helps someone.
<!--break-->
## Unable to resolve superclass

My first problem was that, even though I could create an APK, when I tried to run it on a device I would see a bunch of "unable to resolve superclass" errors in the Logcat console. It looked like some of the JARs I was using (`android-support-v4.jar`, `gcm.jar`, and some third-party libraries) weren't being included in the APK.

I eventually found the answer here: http://stackoverflow.com/questions/16583786/android-sdk-tools-revision-22-issue

Most of my app's code is in an Android library project, and then there is an application project that uses the library. Apparently revision 22 of the SDK breaks the way that application projects bring in JARs from a library project. To fix this, do the following on both the library project and the application project that uses the library:

0. Right-click the project in Eclipse's Package Explorer and choose Properties.
0. Choose **Java Build Path**
0. Choose **Order and Export**
0. Check the boxes next to **Android Private Libraries** and **Android Dependencies**

After making these changes, do a clean and then rebuild.

With this change, I was able to build an APK that installed and ran on an Android device.

This is apparently a bug with ADT 22. See https://code.google.com/p/android/issues/detail?id=55304


## INSTALL_PARSE_FAILED_NO_CERTIFICATES

After getting the release build working, I tried making a debug build to run in the debugger. I figured it would just work, but I saw this error in the console:

    Installation error: INSTALL_PARSE_FAILED_NO_CERTIFICATES

I verified that I had a `debug.keystore` file, which is what should hold the certificates for a debug build. Sure enough, it existed, and hasn't been changed in a couple of years. I hadn't changed anything about my project or my `debug.keystore`, but it looked like something about code signing has changed with the SDK.

I decided to delete my `debug.keystore` file and let the SDK automatically recreate it. That solved the problem.

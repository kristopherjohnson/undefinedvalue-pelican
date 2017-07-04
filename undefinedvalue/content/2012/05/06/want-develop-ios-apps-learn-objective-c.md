Title: Want to Develop iOS Apps? Learn Objective-C.
Date: 2012-05-06 14:41:42
Category: Blog
Slug: want-develop-ios-apps-learn-objective-c
Alias: 2012/05/06/want-develop-ios-apps-learn-objective-c/
Tags: rant, iosdev


As an iOS software developer, I am often asked whether "we" (a team I'm working with, or someone I'm advising) should avoid using Objective-C and instead use a higher-level or easier-to-learn programming language. In general, my answer is "No". The rest of this post explains why.
<!--break-->
## The Problem

A bit of background: Apple provides a development tool called "[Xcode](http://en.wikipedia.org/wiki/Xcode)" which is what they want developers to use to write iOS apps. Programs are written using a programming language called "Objective-C", which enhances C with Smalltalk-style object-oriented message-passing features. Developers also use a tool called "Interface Builder" to visually lay out user-interface elements. Finally, there is a vast collection of libraries known as the "[Cocoa Touch frameworks](https://developer.apple.com/technologies/ios/cocoa-touch.html)" which provide the programming interfaces to all the cool stuff that iPhones and iPads can do. 

While many iOS developers enjoy the nature of Objective-C, many others think it is a terrible language for application development. Writing code in Objective-C seems very complicated to people accustomed to writing applications in C&#x266f;, Java, Ruby, Python, Javascript, and other more modern languages. Many would-be iOS developers don't know C and don't want to learn it. Objective-C developers have to think too much about memory management and other low-level aspects of their applications. Apple is the only company that uses Objective-C, so those who would like to reuse code across different platforms are frustrated due to its non-portability. The Xcode environment has many detractors, and even its fans admit that its bugs and quirks can be maddening.

I am not going to defend Objective-C or Xcode. Many iOS developers would like to use other programming languages and tools.

## The Alternatives

The alternatives to Objective-C and Xcode can be grouped into two categories. One category is the set of tools that allow developers to write their apps in other programming languages, using some sort of bridge to the Cocoa Touch frameworks, which are then compiled down to native code just like Objective-C is. Examples of this category are [MonoTouch](http://xamarin.com/monotouch) (for C&#x266f;) and [RubyMotion](http://www.rubymotion.com/) (for Ruby).

The other category is the set of tools that allow developers to use HTML/CSS/Javascript to write webapp-style code, which is then packaged as something that will run as a native app.  These tools provide some means to access the raw Cocoa Touch frameworks if desired, but the real purpose is to shield developers from them. Examples of these are [PhoneGap](http://phonegap.com/) and [Titanium Appcelerator](http://www.appcelerator.com/). 

## My Advice

For most developers, my advice is to stay away from these things. Go ahead and evaluate them, and maybe one of them is a good fit for your particular set of circumstances, but if you don't know that you have a good reason to use them, just bite the bullet and learn Objective-C.

Here's why: Developing a good iOS app requires use of the Cocoa Touch frameworks. Learning how to use those frameworks is what is difficult about iOS development. Learning Objective-C should take a competent programmer only a day or two, but learning the frameworks is a never-ending struggle. Apple's documentation and samples for the frameworks use Objective-C. Most of the third-party libraries and other components you will want to use are in Objective-C. The smart people who answer iOS development questions in online forums use Objective-C.

if you are using another programming language to interface with all this Objective-C stuff, you end up with these little walls you have to hop over a lot. I'd prefer not to build those walls. [The RubyMotion review by Matt Aimonetti](http://merbist.com/2012/05/04/macruby-on-ios-rubymotion-review/) describes how difficult it can be, especially for beginners.

The only exception to this rule is if you can create a good webapp-style app using PhoneGap or Titanium Appcelerator. The big benefit of this approach is that you can reuse or share HTML/CSS/Javascript code across platforms, so when your iOS app is done you can release versions for Android, Windows Phone, and other platforms with a minimal amount of additional work.

But when you take this approach, you will end up with a webappish app, not an app that takes advantage of what makes iOS special (or what makes any other platform special). Maybe that's the right solution for you, but you'll have to accept that some users will react by saying "Eww, this feels like a webapp".

## The Right Tool for the Job

In general, it's a good idea to use whatever tools and APIs are officially supported by your vendor. If you are doing iOS development, that means you should use Objective-C and Xcode. If you are doing Android development, use Java and Eclipse with the Android Development Toolkit. If you are doing Windows development, use C&#x266f; and Visual Studio. Going with other solutions might have benefits, but whenever you choose an unsupported development environment, you are taking a big risk. At any time, the vendor might make changes to its APIs or toolchain that break all tools you rely upon.

Using the right tool for the job is a good idea. Using anything other than Objective-C to develop iOS apps results in more work and more risk. Just go ahead and learn it. You might even like it.

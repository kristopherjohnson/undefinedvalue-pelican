Title: My Visit to Android-land
Date: 2011-09-11 23:50:52
Category: Blog
Slug: my-visit-android-land
Alias: 2011/09/11/my-visit-android-land/
Tags: android


I've been a happy iPhone and iPad user for a while, but I'm currently involved in developing Android applications, so I decided to buy an Android phone to use for a few weeks. It's important to understand the user-interface conventions and user expectations for whatever platform you are developing for, and I figured that the only way to learn those things would be to take the plunge and immerse myself in Android for a while.

The following is a self-indulgent review of what I've found. If you are an Android fan, you will probably summarize it as "Surprise! Apple fanboy doesn't like Android," and you can just stop reading here.
<!--break-->
## Context

I'll quickly run down my background and biases, so people can understand some of my expectations and reactions.

I got my first Apple computer, a Macintosh SE, in 1987. I immediately felt that Apple understood how computers should look and work. My enthusiasm for Mac&nbsp;OS waned in the late 1990's as Apple stuck with their rickety tinkertoy OS, and I became a GNU/Linux user for a few years. I bought an iMac&nbsp;G5 in 2004 and my enthusiasm for the Apple way was restored.

However, while my personal computers have mostly been Macs, 90% of my income for the past 19 years has come from developing Windows applications, and most of the rest has come from developing UNIX applications, so I'm not ignorant of how other systems work. For what it's worth, I think Windows 7 is about even with Mac&nbsp;OS&nbsp;X 10.6 and 10.7 in terms of providing a good user experience. I stick with Macs because the hardware looks and feels better than the low-margin Wintel hardware that's on the market, and I don't mind paying more for something nice. I also like having a home computer that is nothing like my work computer.

I've long been a fan of mobile computing. When I was a kid, I wanted an iPad, but nobody made an iPad until 2010. So in the meantime I've had an Apple&nbsp;Newton, a few Palm&nbsp;OS devices, a few Windows&nbsp;CE/Pocket&nbsp;PC/Windows&nbsp;Mobile devices, and a couple of never-officially-released products (anybody remember the [Agenda VR](http://tuxmobil.org/pda_linux_agenda.html)?). The iPhone was the first pocket-sized computer that did not completely suck.

While I am a fan of Apple's products, I don't like many of its policies toward consumers and developers, and I've wished for high-quality alternatives. I [looked at Android phones back in 2009](https://undefinedvalue.com/2009/11/19/switching-away-apple), hoping that I'd like them enough to switch away from Apple's ecosystem. Unfortunately, [I was disappointed](https://undefinedvalue.com/2009/11/25/android-maybe-not) with the quality of Android phones and software, and it seemed clear to me that nobody was going to get rich developing software for a system that was marketed as a low-cost alternative to Apple's products. iPhone users are willing to pay for software, and Android users expect everything to be free, so it seemed obvious that if I wanted to make a living as a mobile-software developer, the iPhone market was the place to be.

I've been doing some iOS development, and I am now involved in porting iOS apps over to Android. As stated above, I think it's important that developers and designers deeply understand the conventions of the platforms they are developing for, and so I decided to buy an Android phone and put my iPhone away for a while.

## The Hardware

I had two primary criteria for choosing an Android phone:

- I wanted a "typical" Android phone. That is, I wanted one with display resolution, CPU speed, RAM, and features that would be close to what a majority of Android users would be using. So I didn't want the newest, most feature-packed phone, nor an old clunker.
- I wanted a phone that would work on the AT&T network, so that I could just swap the SIM from my iPhone into it, rather than paying for another data plan or relying on wi-fi.

The result is that I bought a used Samsung Captivate (Galaxy S) via eBay. The Galaxy S is last year's model, but so is the iPhone&nbsp;4, so I think it's fair to compare them. I know there are better Android phones out there, so please don't write me to tell me that your Nexus S or Atrix have none of the problems I mention in this review. I don't care.

Here are some things I like about the Captivate:

- The display is bright and crisp (not as nice as the iPhone 4 retina display, but pretty close).
- The built-in speaker seems to be a little bit louder than the iPhone's. (I often listen to podcasts using the built-in speaker, and the iPhone's low volume has always bugged me.)
- I haven't had a dropped call yet. (But I only have about two phone calls per week, so the sample is small.)

Here are some things I don't like about the Captivate:

- It's too big, and the buttons are awkwardly placed. I'm sure some people like the large display size, but I find it difficult to hold it and operate it with one hand. Even with two hands, it doesn't feel right. (Your hands may vary.)
- It's hard to tell which way is up. The iPhone has this problem too, but the big home button on the iPhone is easier to find when it's in your pocket or when it's dark.
- It feels plasticky and flimsy. I have dropped it a couple of times, and it didn't break, so It's not fragile, but it does feel like a kid's toy.
- It is loaded with a bunch of AT&T crapware.
- AT&T has disabled installation of apps from "unknown sources", so the Android Market is the only place one can get apps. One can't get apps from the Amazon Appstore for Android or from developers who post free apps online. (There are various workarounds for this, but it's annoying.)
- The hardware buttons (Menu, Home, Back, and Search) are not actual buttons, but are just little touch-sensitive areas at the bottom of the phone's case. I'd prefer something I can feel.
- Battery life is terrible. If I just leave it in my pocket all day, then it's fine, but if I use it as often as I use my iPhone, I have to recharge it a couple of times per day.

I would have liked to try an Android tablet as well, but the app I'm porting is a phone app, not a tablet app, so I couldn't justify the purchase. Also, I keep hearing that _next year's_ Android tablets will be really awesome, so I'll keep waiting until that year comes.

## The Software

I hate to have to say what every other iPhone user says about Android, but here it is anyway: Android software is not as attractive and does not work as smoothly as iPhone software does. This is true both of built-in applications and third-party applications. Of course, the best Android apps look better than the worst iPhone apps, but as a rule, Android just isn't as good in the UI department. Default fonts look terrible, and are often way too big or way too small. Scrolling isn't smooth.

It reminds me of using Remote Desktop Connection or VNC to access a remote computer. Everything works, but there's always a slight delay and loss of resolution that takes away the illusion of direct manipulation.

As someone who develops both iOS and Android software, I can understand why this happens. Almost by default, iOS apps look nice. If you just throw a few of the standard UI gizmos into an app, without any additional customization or tweaking, the app will look pretty good. In contrast, Android's standard UI gizmos do not look good. Any really nice Android app you see probably has a lot of highly customized UI code. And if you do get it to look good on one model of Android phone, chances are that it will not look as good on all the other models of phone due to differences in screen sizes, resolutions, aspect ratios, graphics chipset, color schemes, fonts, etc., etc., etc.

The text editing experience is really bad. Unlike iOS, there is no magnifying loupe that appears when you want to finely position the cursor, so trying to place the cursor can be frustrating. Copy/paste is awkward. Many text-editing apps don't have an Undo feature. ("Who the hell does a lot of text editing on their phone," you ask? I do.)

There are some things I really like about Android:

- Alternative input methods are welcome. The Swype keyboard is awesome. I really wish Apple would license this.
- Home-screen widgets are cool. (On the other hand, Live Wallpapers are a demo that got out of hand.)
- The notifications system is nice. (Apple will be providing a similar feature in iOS 5.)
- I haven't really needed "true multitasking", but it is nice that all Android apps are capable of downloading updated content in the background.
- Google Maps navigation is nice.

Much has been written about how horrible the Android&nbsp;Market is in comparison to the App&nbsp;Store, but I didn't find it to be a problem. Yes, there is a lot of crap in there, and it's frustrating when someone tells you "You need application X", and you search for "Application X" in the Market, and there are 20 matches. However, the App Store has a lot of crap in it too, and everyone knows that the way to find good software is by word of mouth and reviews from trusted sources, not by searching the store.

I easily found Android replacements for most of the iOS apps I depend upon. The only exception is the Omni Group's OmniFocus app, which is not available for Android. Fortunately, I can still run OmniFocus on my iPad and MacBook, so missing it on my phone is an annoyance rather then a deal-breaker.

While choice is good, it also has its downsides. Out of the box, my Captivate had five or six different apps that could play music, and I didn't know which one I should use. I'd prefer that there be exactly one standard built-in music player, or SMS app, or app launcher. It's great to have alternatives, but don't force a new user to make choices that they are unqualified to make.

iTunes is one of the worst applications in the world, but I do like that there is a standard way to sync an iOS device with my laptop. I miss that with Android. (Yes, I know about DoubleTwist.)

I haven't rooted the phone. I also haven't jailbroken my iPhone. Ten years ago when I was trying out a new Linux distro every week, I would have loved the chance to try a bunch of different ROMs and OS customizations in my phone. Nowadays, I just don't have time for that. If the product isn't useful out of the box, I don't want it.

## Closing Thoughts

I used the Captivate as my primary phone for about five weeks. I was very happy to go back to the iPhone, but Android really isn't that bad. If Apple ever did anything that really pissed me off, switching to Android wouldn't be a great hardship.

I would still recommend an iPhone over an Android phone for a anyone who is not a geek. A big difference between being an iOS user and being an Android user is the degree of customization that is needed. You can buy an iPhone and use it as-is and be happy. In contrast, buying an Android phone is just a starting point&mdash;you'll need to try a lot of different apps and tweaks before it works the way you want it to work. But if you are a geeky control-freak, then Android does offer more opportunity to get a phone that works exactly the way you want.

The "open" nature of Android doesn't impress me. It's nice that one can download the source code and tweak it, but there are limits to the openness. Google doesn't release new versions of the software until it is shipping on new devices, and the whole development process is quite secretive. Handset manufacturers and carriers add their own restrictions on top of whatever Google provides, so even if Android were truly open, you're still at the mercy of the OEMs and carriers. I will never be able to get an OS upgrade for this year-old Captivate. I'd rather be subject to Apple's control than AT&T's.

My biggest beef with Android is that the whole thing just feels like a second-rate knockoff of the iPhone and iPad, and I've never liked using second-rate products. Palm and Microsoft have been trying some interesting things with their mobile platforms, but the folks at Google are simply engaged in mimicry. If Google can't innovate, then I hope they will steal some good ideas from those other platforms rather than just following in Apple's footsteps. If they are going to just keep copying Apple, I wish they'd do a better job of it.

I disagree with those who claim that Apple is evil and Google is good. Apple wants me to pay them lots of money for stuff I like. Google wants to give me a cheap operating system so that it can sell my data and attention to advertisers. I prefer Apple's offer.

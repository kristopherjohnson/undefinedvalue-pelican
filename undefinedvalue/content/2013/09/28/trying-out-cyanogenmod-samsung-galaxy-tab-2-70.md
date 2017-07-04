Title: Trying Out CyanogenMod on a Samsung Galaxy Tab 2 7.0
Date: 2013-09-29 04:35:59
Category: Blog
Slug: trying-out-cyanogenmod-samsung-galaxy-tab-2-70
Alias: 2013/09/28/trying-out-cyanogenmod-samsung-galaxy-tab-2-70/
Tags: galaxytab, cyanogenmod, android


Last year, I bought a [Samsung Galaxy Tab 2 7.0](http://en.wikipedia.org/wiki/Samsung_Galaxy_Tab_2_7.0) for use as an Android development/testing device. I didn't expect it to be good, and it wasn't. It was slow, clunky, and ugly in comparison to the iPad, just like every other Android tablet. But it was cheap, and I only used it to test apps I was developing, so it didn't bother me much.

Earlier this year, it finally got an upgrade to Jelly Bean, which improved the slow/clunky aspects, but it still wasn't good. I bought a new Nexus 7 in July (which is an awesome Android tablet), so I went to [gazelle.com](http://www.gazelle.com) to see what they would give me for a used Galaxy Tab 2 7.0. Their offer: $16.

So, it went into the old-devices drawer. I kept it only because I might need it in an emergency if my Nexus 7 died at the worst possible time.

When all the [news](http://www.cyanogenmod.org/blog/a_new_chapter) and [drama](https://plus.google.com/106978520009932034644/posts/L8FJkrcahPs) about [CyanogenMod](http://www.cyanogenmod.org/about) (CM) broke last week, I decided I would give CyanogenMod a try. I was curious, and I had a device available to "sacrifice".

And you know what? That crummy old Galaxy Tab 2 7.0 is actually a pretty nice tablet with CM installed. I now have an Android 4.2.2 Jelly Bean tablet without all the Samsung TouchWiz crapware. It's not as good as the Nexus 7, but it no longer feels like junk, and it might stay out of that drawer for a while. 

If you have an Android device in your junk drawer (or a Kindle Fire, or a NOOK), you might want to give CM a try. Read on if you're interested.
<!--break-->
## Installation Pains

Installation wasn't easy, and is not recommended for non-technical users. If you've never flashed new firmware nor installed Linux on a computer, you may find it daunting. I expected problems, and was 50% certain I'd end up with a bricked device, but as I wrote above, this device was just one step away from the trash can anyway.

I followed the instructions on this page:

- http://wiki.cyanogenmod.org/w/Install_CM_for_p3110

I installed the latest stable release, [cm-10.1.3-p3110](http://get.cm/get/jenkins/42539/cm-10.1.3-p3110.zip) along with the corresponding [Google Apps](http://goo.im/gapps/gapps-jb-20130812-signed.zip) package.

I ran into three problems during the process. I'll describe the problems and their solutions here in case anyone else hits the same issues and runs across this page in a search.

### Unable to Install ClockworkMod

Before installing CM, one must install a custom [recovery](http://www.androidcentral.com/what-recovery-android-z) partition that can be used to install CM. The suggested recovery is [ClockworkMod](http://forum.xda-developers.com/wiki/ClockworkMod_Recovery), and installation is described in that *How to Install CyanogenMod* document I was following. However, after following the steps in the document and then rebooting, booting into recovery resulted in me still having the standard default recovery, not ClockworkMod.

I went through the steps a couple more times, and ended up with the same result. "Maybe I'm just not smart enough for CyanogenMod," I thought.

I Googled around. Eventually I stumbled on a forum posting that suggested that the stock ROM might be restoring the original recovery partition, and the trick was to make sure you boot into recovery before that happened. I don't know exactly what I did, but followed the steps one more time, taking care to ensure that I booted into recovery immediately after the downloader said it was finished, and it worked. I was in ClockworkMod!

### Unable to Install zip from sdcard

Once in ClockworkMod recovery, I was supposed to be able to choose the *Install zip from sdcard* menu item and then select the `cm-10.1.3-p3110.zip` file that I had earlier copied to the device's `/sdcard` directory. But when I selected that command, the file wasn't visible in the resulting list.

I rebooted into the normal device OS, and verified that `cm-10.1.3-p3110.zip` was indeed in the `/sdcard` directory. Booted into recovery again, and again, unable to select that file.

So, I chose the *Install from sideload* command instead, and then did `adb sideload cm-10.1.3-p3110.zip` from my Mac connected via USB. That worked. I then did the same thing with the Google Apps package.

Subsequent research indicates that the zip files can be found by ClockworkMod in the `/sdcard/0/` directory, rather than in `/sdcard/`. This has something to do with support for multiple users.

### Keyboard Not Functional

After sideloading the CM and Google Apps packages, I rebooted the device, and CyanogenMod appeared on the screen. Success!

Well, not really. It asked me whether I wanted to set up a CyanogenMod account, and I clicked the button, and then it brought up the wi-fi selection screen, and I selected my wi-fi, and then it asked me for a password.

But no keyboard was displayed. How does one enter a wi-fi password without a keyboard?

So I just skipped through all the initial setup stuff. After I got to the Android home screen, every few seconds I got an error alert saying "Unfortunately, Android keyboard (AOSP) has stopped", indicating that the standard Android keyboard process was crashing repeatedly. That explained why no keyboard was displayed when I was prompted for my wi-fi password.

My first thought was to install [SwiftKey](http://www.swiftkey.net), my preferred Android keyboard. But how does one download something from Google Play if one can't enter the wi-fi password?

So, more Googling. The most popular suggested fix for this problem was to go into Settings > Apps and clear data for the Android Keyboard and Dictionary Provider apps. I tried this, and it didn't help.

Another popular suggestion was to try an older version of the Google Apps package. It didn't make sense to me that the Google Apps package would affect the standard Android keyboard, but I checked for older compatible Google Apps packages anyway.

And this is how I discovered I had installed the wrong Google Apps package. I had installed the package designed for CM 4.2, but I had CM 4.1.

So I rebooted back into recovery and installed the correct Google Apps package via sideload. For good measure, I also cleared the user data, the Dalvik cache and every other thing that seemed clearable or resettable in ClockworkMod.

I rebooted, and the keyboard worked.

## The Result

I expected CyanogenMod to be weird, but it isn't. It generally looks and works just like my Nexus 7 does. I can access my Google contacts, calendar, and mail. I can download and run my purchased apps from the Google Play store (although there are a couple that are marked "incompatible with your device"). I can read my Kindle books. I can access all my Dropbox stuff.

I do see a few extra menu items in Settings, and there are probably a few magic features I haven't noticed yet, but if you are accustomed to pure Android as delivered in the Nexus devices, you'll find it familiar.

## The Community

As with any large open-source project, the community of developers and users are the only source of help. The CM community is a lot like the Linux community: there are a few smart helpful people, a few users sincerely offering and seeking assistance, and a lot of arrogant assholes who want to make everyone feel stupid.

Don't be part of that last group.

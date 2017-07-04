Title: Getting Root on Huawei U8665 Fusion 2 Phone
Date: 2015-02-20 00:33:07
Category: Blog
Slug: getting-root-huawei-u8665-fusion-2-phone
Alias: 2015/02/19/getting-root-huawei-u8665-fusion-2-phone/
Tags: root, huawei, android


I've had an old [Samsung Galaxy S Captivate](http://undefinedvalue.com/2011/09/11/my-visit-android-land) phone, running Android 2.2, that I've used as a test device while developing Android apps. In my new job, I no longer need to support Android 2.2 (hooray!), but I do need to support Android 2.3 (boo!). I tried installing [CyanogenMod](http://www.cyanogenmod.org) to update the Captivate to Android 2.3, but I ended up bricking the device.

Rather than spend more time trying to figure out how to fix that, I looked around for a cheap new Android 2.3 device, and found the [Huawei U8865](http://www.amazon.com/Unlocked-Android-Touchscreen-Bluetooth-Microsd/dp/B00BGYOO60), also known as the "Fusion 2", for $60. That seemed like a reasonable price for a brand-new old phone, so I purchased it and it arrived the next day.

Unfortunately, when I tried using it for development, I hit a snag. My work requires using [`adb shell`](http://developer.android.com/tools/help/adb.html) and related utilities, and whenever I tried those, I just got a "permission denied" response. I couldn't even take a screenshot.

I looked around for instructions to "root" the phone (that is, get privileged access). They aren't hard to find, but the people who write up these instructions all assume that (a) their readers have no idea what they are doing, and (b) everybody uses Windows. Neither of those are true for me, so I had to translate those instructions into developer-speak.

So, anyway, if you are running Mac OS X and you already know how to use Terminal and `adb`, then here are instructions for you:

(These instructions are based on those at <http://androidforums.com/threads/step-by-step-root-walkthrough-for-huawei-fusion-2.685504/>.)

1. Download <https://www.dropbox.com/s/qtc37pley0vinj8/Huawei-Fusion-2-Recovery-Root.zip> and extract the contents.
2. Open Terminal and `cd` to the extracted `Huawei-Fusion-2-Recovery-Root/Huawei-Fusion-2-Recovery-Root` directory
3. Turn off phone
4. Reboot phone into fastboot by holding Volume Down and Power buttons simultaneously for 10-20 seconds. (It will freeze at the AT&T logo.)
5. Connect phone to computer.
6. Type `fastboot devices` to verify phone is connected.
7. Type `fastboot flash recovery recovery.superrecovery.img`
8. After it finishes, unplug phone.
9. Remove back of phone, remove battery, wait 15 seconds, then re-insert battery and attach back.
10. Hold Volume-Up and Power button simultaneously until it boots into recovery (15-20 seconds of holding both buttons)
11. In recovery menu, select the "reboot device" option with the volume buttons (it should already start with reboot highlighted) and press the power button to reboot. 

After that, you will "have root". So if you use `adb shell` to get a command shell on the device, you can run `su` to get superuser privileges. There is also a new [SuperSU](https://play.google.com/store/apps/details?id=eu.chainfire.supersu&hl=en) app on the phone. 

But that's not really what I wanted. What I want to do is run `adb shell <some-command>` from the Mac. If you read the `adb` documentation, you might think you can run `adb root` to enable that, but you will just get an error message saying "adbd cannot run as root in production builds".

One needs to install an alternative version of `adbd`. I downloaded and installed this one from Google Play: [adbd insecure](https://play.google.com/store/apps/details?id=eu.chainfire.adbd&hl=en). There is an option to have it automatically grant superuser access at boot, and I enabled that.

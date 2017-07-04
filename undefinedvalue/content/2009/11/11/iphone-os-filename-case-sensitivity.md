Title: iPhone OS Filename Case Sensitivity
Date: 2009-11-12 00:51:59
Category: Blog
Slug: iphone-os-filename-case-sensitivity
Alias: 2009/11/11/iphone-os-filename-case-sensitivity/
Tags: iphone


I hit a little snag while adding a feature to an iPhone app today. I added this code to load a logo to be displayed in a view:

    UIImage *logoImage = [UIImage imageNamed:@"Icon.png"];

This worked fine in the iPhone Simulator, so I thought I was done. I loaded the app onto my iPod Touch, and it didn't work. Running in the debugger, I discovered that `logoImage` was being set to `nil`.

Why would this not work on a device, when it ran fine in the simulator?

It turns out that the iPhone OS filesystem is case-sensitive, while the Mac OS X filesystem is not case-sensitive. The actual name of the image file was `icon.png`, with a lowercase-_i_, so it didn't match on iPhone OS.

No big deal, but it's another reminder that you always need to test on an actual device before considering an iPhone development task _done_.


Title: Netgear ReadyNAS Duo 2000 Setup and Review
Date: 2009-08-20 00:40:10
Category: Blog
Slug: netgear-readynas-duo-2000-setup-and-review
Alias: 2009/08/19/netgear-readynas-duo-2000-setup-and-review/
Tags: sysadmin, review, readynas, netgear, backups


I have previously written about my [backup strategy](http://undefinedvalue.com/2007/10/26/backups). I've never really worried about backups too much. In the 30 years I've been using computers, I've never lost a hard drive.

...until last weekend. My wife's MacBook Air was displaying some funny behavior, so I ran Disk Utility on it. Disk Utility said the drive had problems, so I clicked *Repair Disk*, and it would not boot thereafter. I called Apple, and their expert told me I'd have to erase the drive and reinstall the operating system. We had no backups for that machine. My wife was not happy to lose everything. And of course, it is *my* fault she had no backups. (I've told her about Time Machine, but she didn't believe it could really be that easy to set up, so she never did.)

So, better late than never, I decided to get some network storage and start backing up everything to it. A friend was happy with his Netgear ReadyNAS, so I ordered a Netgear ReadyNAS Duo 2000 from Amazon, along with two 1-TB Western Digital Caviar Green hard drives. Total price came out to about $400.

The ReadyNAS has two drive bays. Most models come with a drive included, but I bought the "bare" one that has no preinstalled drives, assuming that it would be cheaper to buy my own drives. Upon reading the manuals, I immediately hit a problem: the manuals explain how to add a second hard drive to a ReadyNAS that comes with a single drive, but nothing about what to do if you have an empty ReadyNAS.

Hoping for the best, I installed the two Caviar drives in the NAS, plugged it into the network, plugged it into power, and hit the power button. It turned on, but the slowly blinking LED didn't give me a warm fuzzy feeling.

I installed the RAIDar software, which one uses to manage the device, and it told me I had bad disks.

After about half an hour of Googling, registering the product, registering for the Netgear forums, and registering for the ReadyNAS forums (each of which required separate sign-up forms and e-mail confirmations), I finally found a current [ReadyNAS FAQ](http://www.readynas.com/forum/faq.php) (after hitting a few old FAQs that were created before my model existed). There was nothing specific about my situation, but I decided I would try the "factory reset". That worked: RAIDar enabled its Setup button, and I was able to initialize everything.

I was initially worried about the fan noise. When the ReadyNAS boots up, the fans are incredibly loud for something that small. After 30 seconds or so, the noise drops a little, but it was still really loud. A Google search for "readynas loud fan" indicated that lots of users have replaced their ReadyNAS fans, due to the noise. But after the drives got formatted, the fan noise dropped to a barely detectable level. It's not as quiet as my Macs, but it's not loud enough to be annoying.

It was very easy to set up [Time Machine with the ReadyNAS](http://www.readynas.com/?p=1097). (First thing I did was back up my wife's Air, of course.)

The ReadyNAS has a lot of other features that I am not yet using. $400 for a backup solution seems a little pricey, when one can buy a 1-TB drive and enclosure for about $100, but having storage available on the network means we're more likely to actually do backups. We'll see how things go.

A complete description of all the features can be found here: http://www.readynas.com/?p=177

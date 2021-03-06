Title: Backups
Date: 2007-10-26 11:32:00
Category: Blog
Slug: backups
Alias: 2007/10/26/backups/
Tags: sysadmin, backups


<p>
I've never been good at keeping backups.  Back in the good old days, when all my data fit on one floppy disk, I made copies of those, but the first time I had to back up a 20-MB (yes, <i>megabyte</i>) hard drive onto a stack of floppies, I gave up on backups.  As my hard drives have grown, the thought of spending time making huge backups have become more daunting.
</p>
<p>
I've been lucky.  I've never had a hard drive crash, or lost a laptop, or otherwise been unpleasantly surprised.  I've never been taught a harsh lesson about the importance of backups.  For important files, I've e-mailed copies to myself, taking advantage of the practically unlimited free storage space provided by Yahoo! Mail and GMail.  However, if one of my hard drives ever died, it would take a very long time to re-install an OS and all my applications and settings.
</p>
<p>
I've always felt that I should be keeping backups, and with the upcoming <a href="http://www.apple.com/macosx/">Mac OS X Leopard</a> upgrade, I figured I should keep a backup of my Tiger installation in case Leopard turned out to be a lemon.  A <a href="http://jwz.livejournal.com/801607.html">recent post by jwz</a> about backups prompted me to get serious.  His suggestion is basically to buy some extra hard drives and an external enclosure, make copies of your hard drives, and use <a href="http://samba.anu.edu.au/rsync/">rsync</a> to periodically copy changes from your main drives to the backup copies.  This gives you a bootable backup drive, so if your real drive ever dies, you just pop the backup drive into your computer, and you're back in business.  jwz's advice is sound, and is easy to follow if you have a Mac or a Linux box.  It's a little expensive to buy so many spare drives, but the convenience of having bootable backups is worth it to me.
</p>
<p>
Unfortunately, it is not as easy to back up a Windows machine.  You can use rsync if you have <a href="http://www.cygwin.com">Cygwin</a> installed, but I wasn't sure that I would trust that to give me a bootable backup.  So, my strategy for now is to use <a href="http://www.acronis.com/homecomputing/products/trueimage/">Acronis True Image</a> to make a backup copy of my drive, and then use <a href="http://www.microsoft.com/windowsxp/using/digitalphotography/prophoto/synctoy.mspx">Microsoft's SyncToy</a> to periodically copy new files from the laptop to the backup drive.
</p>
<p>
One benefit of this strategy is that it has been easy to upgrade my hard drives.  My MacBook only had a 60-GB drive, which got full pretty quick; now it has a 160-GB drive with plenty of extra space.  I also grew my Windows laptop drive from 120 GB to 160 GB.
</p>
<p>
I'll play around with the "Time Machine" feature of Leopard, but I'll probably keep relying on the simpler backup strategy instead of Apple's slick magic stuff.
</p>

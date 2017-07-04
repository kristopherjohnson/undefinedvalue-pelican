Title: Leopard Upgrade
Date: 2007-10-28 06:55:00
Category: Blog
Slug: leopard-upgrade
Alias: 2007/10/28/leopard-upgrade/
Tags: mac, leopard


<p>
I've upgraded my MacBook from Tiger to Leopard.  I hit a couple of snags along the way; maybe this will help someone else avoid the same issues.
</p>
<p>
1.  When I first attempted to upgrade, the Installer wouldn't allow me to select my hard drive for the upgrade.  I have been using a copy of my original hard drive, and the copy was apparently not partitioned with "GUID Partition Table."  It was booting fine under Tiger, but apparently there are new rules for Leopard.  The installer offered to erase my drive for me and partition it correctly, but I didn't want to lose all my applications and data.  The moral:  when partitioning a new drive for use as a boot disk, click the <b>Options...</b> button in Disk Utility's <b>Partition</b> page and select "GUID Partition Table" (the default selection is "Apple Partition Table"). 
</p>
<p>
2.  After installation, the drive started booting, but then just sat on a blank blue screen for a long time.  This is apparently caused by an old version of Unsanity's Application Enhancer.  To remove this software and let Leopard boot, follow the "Solution 2" instructions given here: <a href="http://docs.info.apple.com/article.html?artnum=306857">http://docs.info.apple.com/article.html?artnum=306857</a>.
</p>
<p>
3.  My wireless Mighty Mouse didn't work at first.  The Bluetooth icon didn't show up in the System Preferences, and the menu bar showed the icon but the menu said that Bluetooth was unavailable.  After rebooting a couple times, Bluetooth magically reappeared and the mouse worked as before.
<p>
After getting over those little bumps, Leopard appears to be working fine, and it is worth noting that the serious problems would not have occurred if I was using the original Apple-installed hard drive and I had not installed any hacky software.  So, can't blame Apple.
</p>

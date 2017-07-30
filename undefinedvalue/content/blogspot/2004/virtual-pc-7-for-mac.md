Title: Virtual PC 7 for Mac
Date: 2004-10-30 19:25
Author: Kristopher Johnson
Tags: virtualpc, mac, microsoft
Slug: virtual-pc-7-for-mac

I received Office 2004 Professional for Mac a couple of days ago. I
haven't felt like searching around for my Office 98 CDs (which I assume
will be needed for installation of this upgrade version), so I haven't
tried Office on the Mac yet. I was entertained by the packaging, which
was designed to appeal to the dreamy stupid hippie-geeks that Microsoft
believes Mac owners to be.

I did install Virtual PC 7, which is in a separate package from the rest
of the Office install. Installation was easy, including automatic set up
of a Windows XP Service Pack 2 virtual machine. This was a nice
surprise: at work I've had to set up a few Virtual PC virtual machines
on Windows boxes, and I've found that doing a full installation of an
operating system on a virtual machine takes a very long time and can be
problematic when the OS installer doesn't automatically recognize the
virtual devices.

The first things I did after getting VPC installed were to try Windows
Update, and to try to activate Windows over the Internet. Neither
operation worked due to connection errors. I tried disabling the
firewalls, but that didn't help. (BTW, when VPC is running, you no
longer have access to the built-in Apple firewall.) What finally worked
was to change the VPC network settings from "Shared Networking" to
"Virtual Switch", which gives the virtual machine its own IP address.
There were warnings that Virtual Switch might not work with a wireless
network connection, but it is working fine for me and my AirPort
connection.

VPC seems to be well behaved. When it is idle (that is, when I'm not
"doing something" with the virtual machine), it uses between 2% and 12%
of my Mac's CPU. Even when it is busy, it doesn't bog down my other
running Mac apps.

There is a lot of integration between the virtual machine and the rest
of the Mac. For example, you can drag files between the Mac desktop and
the Windows desktop. Windows processes show up in the Mac's Activity
Monitor process list, and you can Quit or Force Quit the Windows
processes from the Mac. Windows things show up in the Dock. I'm not sure
whether I like these features. I supposed they are helpful for people
who need to use both Windows and Mac OS X to get things done, but I
worry that VPC might be making my Mac less stable and secure.


Unfortunately, Virtual PC is really, really slow on my iMac G5. I didn't
expect it to be speedy, but it is too slow to be useful for anything. So
when I want to run Windows apps from my Mac, I'll use Remote Desktop
Connection to access the real Windows PC that is in the other room. When
I have some free time, I'll try installing Fedora, Gentoo, or one of the
other Linux distros to see what kind of performance I can get from a
less-bloated OS.


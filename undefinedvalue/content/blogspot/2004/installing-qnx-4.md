Title: Installing QNX 4
Date: 2004-03-03 05:38
Author: Kristopher Johnson
Tags: qnx
Slug: installing-qnx-4

I installed [QNX](http://www.qnx.com) 4 on a machine today, for some
upcoming embedded systems work. This is not the first time I've
installed it, but of course I didn't take any notes the last time I did
it, so it was almost a new experience.

My first hurdle was figuring out how to run the installer. The
installation program runs on Windows, but the machine where I wanted to
install only had Linux.

"No problem," I thought, "it's a bootable CD, so I can just boot from
that". My next hurdle was the discovery that while the machine had a
CD-ROM drive inside it, there were no power or data cables connected to
it. And there was a good reason for that: the drive didn't have an IDE
interface, but something with a whole lot more pins than any ribbon
cable I could find. So I scrounged up another CD-ROM drive and plugged
it in. Then it took several minutes of rebooting and cursing before I
had to conclude that the ancient BIOS on that 300 MHz Pentium II machine
wouldn't let one boot from the CD.

I was starting to think I'd have to install Windows on that machine just
so I could run the installer for QNX. This would have been a problem,
because this was a CD-ROM drive, and we only have DVDs for installing
Windows. But poking through the contents of the CD, I found a .BAT file
that would create a bootable floppy for installing a demo version of
QNX. I didn't want a demo version, but a few more minutes of poking
around (and guessing) led me to discover how to create a bootable floppy
for installing the full QNX.

So, finally I booted the floppy and went through the QNX installation. I
actually had to do this twice, because the first time I couldn't figure
out how to delete all the Linux partitions to make the entire hard drive
a QNX partition. But I eventually had a bootable QNX box.

The last problem was getting a working network interface. The machine
(which I inherited from a recently departed colleague) had both built-in
Ethernet on the motherboard and a PCI Ethernet card. I tried configuring
both interfaces for DHCP and plugging both into my switch, but neither
card was able to retrieve an IP address. I won't bore anyone with the
details (assuming they are not thoroughly bored already), but I
eventually figured out that there was no driver for the card, and
removing it let the built-in Ethernet port start working. I had to give
it a static IP address at first, but eventually got it doing DHCP by
ignoring the nice network-configuration GUI and instead using
"dhcp.client -h mymachine -i en0 &".

So it wasn't impossible, but this illustrates one of the reasons Windows
is going to remain popular. I've heard people with horror stories about
Windows installs, but every one I've done has been basically (a) boot
with the CD, (b) follow the onscreen instructions, (c) OK, everything
works. Sure, QNX is not a "consumer" operating system, and a lot of my
problems were related to having ancient hardware, but still, I think it
should have been easier.


Title: A Backup Restoration Story
Date: 2014-12-29 03:17:16
Category: Blog
Slug: backup-restoration-story
Alias: 2014/12/28/backup-restoration-story/
Tags: rant, crashplan, backups


For most of my computing lifetime, I didn't bother with backups. They were too much trouble, and back when it took 20 floppy disks to back up a Mac hard disk, they took too much time. But now with services like [Time Machine](http://en.wikipedia.org/wiki/Time_Machine_(OS_X)), [CrashPlan](http://www.code42.com/crashplan/), [Backblaze](https://www.backblaze.com), [Dropbox](https://www.dropbox.com), and [Google Drive](https://www.google.com/drive/), it is pretty easy to keep redundant copies of everything. I had files in these locations:

- my main laptop
- my old laptop (given to stepson for schoolwork), which still had all my files on it from the time before I got the new laptop
- family iMac, which in addition to having copies of my important files also had an external hard drive that held Time Machine backups for all home computers
- CrashPlan (offsite backup)
- Dropbox (which is not really a "backup", but it means it's easy to maintain multiple copies of important files)

So I thought I was pretty well backed up, until a few events happened in a short period of time:

1. My main laptop's SSD filled up with work-related stuff, so I deleted some big non-work-related stuff (Aperture library, virtual machine images), because I knew I had copies of those things on my old laptop, our iMac, and in CrashPlan offsite backup.
2. My old laptop died when the kid dumped a glass of milk on it. So that's one old copy gone, but hey, we have others, right?
3. The external hard drive that held our Time Machine backups failed. So I bought a new external drive and reconfigured Time Machine on all our machines to back up to it. That meant we lost our old Time Machine backups, I didn't worry because I knew I had copies of important stuff on the family iMac, and we'd have fresh new Time Machine backups in no time.
4. The old family iMac died. We were lucky in that Apple botched the repair, and gave us a brand new machine to replace it, but the downside was that we lost everything that was on that machine's internal hard drive.

These events all happened within a month. In hindsight, I wish I'd reacted faster, but at the time, I just thought, "It's OK, we still have other backups."

So, anyway, we get this new iMac, and I figure I can just plug the external Time Machine drive into it and we'll have all our data back. But no: apparently I when I configured all the other family Macs to back themselves up to the family iMac's external drive, I neglected to configure the iMac to back _itself_ up.

I had to fall back to the CrashPlan backup. I am very glad we had it, because otherwise we would have lost our family photo archives and some other important stuff. But the downside is that it has taken about five days to restore everything from CrashPlan. I don't know whether to blame our ISP or CrashPlan for the slowness of the restoration, but being unable to use that new machine for five days has been annoying.

CrashPlan's restoration functions suck. When I set up the CrashPlan app on the new iMac, it asked whether I would like to synchronize that new iMac with the old iMac's backup. "Sure, that would be awesome" I thought, and I clicked Yes. Then it took _two days_ for the synchronization to complete, and during that time I couldn't restore anything.

Then, when synchronization finally completed, I checked the box to restore the entire hard drive and clicked the _Restore_ button. CrashPlan spent a couple of hours counting up how many files that was and how big they were, and then it crashed. I tried again, waited a couple of hours again, and it crashed again. (So you need to have a plan for when CrashPlan crashes.)

Because it apparently couldn't restore the entire hard drive at once, I selectively restored individual folders (`Applications`, `/Users/kdj`, `/Users/pebble`, etc.). This worked, but again I had to sit at the computer for a long time while CrashPlan counted up all the files, because after selecting something, you can't click _Restore_ until it finishes counting them up.

And then after restoring, I noticed some files missing, so I had to go back into CrashPlan and play with the options to get it to restore files from the date our old iMac died, and to include deleted/hidden files.

So, lessons learned:

- Make sure _all_ machines are backing up to Time Machine. Check this every week or so.
- Restoring from CrashPlan sucks. Maybe that's just the nature of restoring a few hundred gigabytes of data over the Internet, but I may look into [other options](https://www.backblaze.com) when my annual subscription expires.
- When some link in the backup chain breaks, fix it right away.

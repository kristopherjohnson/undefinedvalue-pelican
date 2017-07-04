Title: Embracing Customization and Automation
Date: 2012-12-09 23:00:59
Category: Blog
Slug: embracing-customization-and-automation
Alias: 2012/12/09/embracing-customization-and-automation/
Tags: scripting, productivity, automator


During the first decade-or-so of my career (the 90's), I had to use a lot of different computers. I worked on half a dozen different operating systems, and during the course of a day it was common to use four or five different computers, only one or two of which were in my cubicle. I'd spend weeks at customer sites. I often sat side-by-side with other developers to work through issues. Every few weeks, a new machine would appear or another machine would disappear.

This led me to decide that I should never treat any computer as "mine", no matter how often I used it or how little anyone else used it. So I didn't spend time customizing any of the system or application settings to suit me. I didn't mess with the keyboard bindings. I didn't write a lot of scripts or macros. I tried to become as adept as possible at using the "stock configuration" of every tool. The extent of my customization was copying a `.emacs` file from machine to machine.

This habit was reinforced when I got into Windows development, and found that I needed to re-install Windows from scratch every couple of months to keep things running well, and that I had to help non-technical users figure out how to fix their machines. Sticking to the stock configuration and standard applications seemed to be the only way to stay sane.

I often rolled my eyes when I'd hear someone talk about how hyperproductive they were with their Dvorak keyboard layout and customized desktop shell and macro recorders. "Great", I'd think, "but can you also be productive with the computer in the neighboring cubicle, or the computer at your parents' house?"  I was proud that I could sit down in front of any computer, and not need to worry about how to work without All My Stuff with me. As the Buddhists say, attachment is the cause of suffering, so let go of your attachments.

Over the past couple of years, I've finally started to relax this stock-configuration-only policy. A few things have changed:

- I do practically all my work with my own personally owned laptop. I always have it with me, at every work location and at my home. Even when I have to do something with another computer, I often do so by connecting to it from my laptop. So my machine really is "mine", and I rarely touch another.
- Dropbox, iCloud, GitHub, and similar services make it easy to keep All My Stuff in sync between machines, and to set up a brand-new machine the way I want it.
- I'm no longer stuck with using Windows most of the time. Mac OS X is a lot easier to customize and automate, due to its UNIX underpinnings. (Yes, seriously.)

Here are the things I've found most useful:

- [Keyboard Maestro](http://www.keyboardmaestro.com/main/): This thing is awesome. Key rebinding was the customization I put off the longest, due to concerns about the need to memorize a bunch of new keyboard shortcuts and the need to find keys that were not already used by my applications, but now that I've dived in, I like it.
- [Alfred](http://www.alfredapp.com): a nice app launcher. I've also tried QuickSilver and LaunchBar, but decided I prefer the simplicity of Alfred
- [TextExpander](http://smilesoftware.com/TextExpander/index.html)
- Automator and the Services menu: While not as useful as they could be, due to Apple's on-again-off-again interest in supporting and promoting them, they are great for hooking little scripts into my workflow.
- Safari Extensions: If you know a bit about JavaScript and the DOM, you can automate a lot of common web activities, and even customize website behavior.

Here are things that I've experimented with, and decided to avoid:

- AppleScript. I use it when I have to, but it is the **worst scripting language ever created**. Whenever I can use bash, Python, or JavaScript instead, I do.
- Application-specific macros. Some applications provide their own mechanisms for replaying sequences of keystrokes or triggering scripts. I use these when they make sense, but it is generally better to let Keyboard Maestro, TextExpander, or the Services menu take care of them system-wide.
- Speech recognition: The Mac has long had a speech recognition system that lets you do a lot of things by just telling it to do so. However, this has never been as useful as, for example, Siri on the iPhone.
- Doing everything suggested by Merlin Mann, Brett Terpstra, Dr. Drang, and MacSparky. Those are all smart people who figure out some cool stuff, but it's easy to get bogged down trying to use it all. It's better to examine your own workflow and improve it than it is to try to adopt someone else's workflow. (It also makes me feel stupid when it takes me longer to *read* that stuff than it takes them to *write* it.)

The process of customizing my computer has changed the way I use it. Whenever I do the same sequence of steps more than a couple of times, I stop and think about whether there is a way to make it faster or easier. Often the answer is not to customize the machine further, but to change my own work habits.

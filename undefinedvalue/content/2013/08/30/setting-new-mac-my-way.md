Title: Setting Up a New Mac, My Way
Date: 2013-08-30 18:02:30
Category: Blog
Slug: setting-new-mac-my-way
Alias: 2013/08/30/setting-new-mac-my-way/
Tags: setup, osx, mac, installation


Over the past couple of weeks, I've set up a few Mac OS X machines to do development of iOS and Android apps. Doing this used to be an all-day chore, but things like app stores, iCloud, and Dropbox have streamlined the process a lot.

(I could streamline the process even more by cloning an existing drive or virtual machine, but I'd rather install everything from scratch to avoid the presence of old cruft.)

As a reminder to myself, and to help out anyone else who needs to do this, here is my procedure for setting up an OS X machine [the way I like it](http://undefinedvalue.com/2012/06/15/my-setup):

0. Install/re-install OS X.
0. During the OS X setup process, use the same login account name and password that I use on other computers, and provide the Apple IDs for iCloud and iTunes (which are different, in my case).
0. Open System Preferences and do the following:
   - In the *General* panel, set *Sidebar icon size* to *Small* and *Show scroll bars* to *Always*.
   - In the *Mission Control* panel, uncheck the *Automatically rearrange Spaces based on most recent use* box.
   - In the *Mouse* and *Trackpad* panels, set all speeds to two ticks less than the maximums, and enable all the gestures.
   - In the *Keyboard* panel, set *Key Repeat* and *Delay Until Repeat* all the way to the right, and check the *Use F1, F2, etc. keys as standard function keys* box
   - In the *Keyboard* panel, go to the *Shortcuts* tab, select *Services*, and then enable the *New Terminal at Folder* service.
   - In the *iCloud* panel, enable everything.
   - In the *Sharing* panel, set the *Computer Name* to something unique (not "Kristopher's computer") and enable *Remote Management*, *Remote Login*, and *File Sharing*.
   - Set up *Time Machine*
   - If this is a virtual machine, go to the *Desktop & Screen Saver* panel and turn off the screen saver, and go to the *Energy Saver* panel and set the sleep sliders to *Never*.
0. Use the *Software Update...* menu item to install any system updates that are available, and reboot if necessary.
0. If this is a virtual machine, install VMWare Tools or Parallels Tools.
0. Download and install these packages (using serial numbers and licenses stored in 1Password):
   - [Dropbox](https://www.dropbox.com/gs) (and wait for everything to sync before continuing)
   - [1Password](https://agilebits.com/onepassword)
   - [TextExpander](http://smilesoftware.com/TextExpander/index.html)
   - [Keyboard Maestro](http://www.keyboardmaestro.com/)
   - [Chrome](http://www.google.com/chrome)
   - [nvALT](http://brettterpstra.com/projects/nvalt/)
   - [Sublime Text](http://www.sublimetext.com)
   - [AppCode](http://www.jetbrains.com/objc/download/)
   - [SourceTree](http://www.sourcetreeapp.com)
   - [OmniOutliner](http://www.omnigroup.com/omnioutliner)
   - [OmniPresence](http://www.omnigroup.com/omnipresence)
   - [MultiMarkdown](http://fletcherpenney.net/multimarkdown/)
   - [Markdown Service Tools](http://brettterpstra.com/projects/markdown-service-tools/) (copy the `.workflow` files to `~/Library/Services`)
   - [MacTeX](http://www.tug.org/mactex/index.html)
   - [Pandoc](https://code.google.com/p/pandoc/downloads/list)
   - [OpenOffice](http://www.openoffice.org/download/index.html) and/or [LibreOffice](http://www.libreoffice.org/download) (depending on mood)
   - [Source Code Pro font](http://sourceforge.net/projects/sourcecodepro.adobe/files/)
   - [Deja Vu fonts](http://dejavu-fonts.org/wiki/Download)
   - [Inconsolata-g font](http://www.fantascienza.net/leonardo/ar/inconsolatag/inconsolata-g_font.zip)
   - [Input font](http://input.fontbureau.com/download/)
   - [CrashPlan](http://www.crashplan.com)
   - [Bartender](http://www.macbartender.com)
   - [Hazel](http://www.noodlesoft.com/hazel.php)
   - [Kaleidoscope](http://www.kaleidoscopeapp.com)
   - [µTorrent](http://www.utorrent.com)
   - [XQuartz](http://xquartz.macosforge.org/)
   - [FreeMind](http://freemind.sourceforge.net/wiki/index.php/Download)
0. Open the App Store app and install these applications (skipping any that are not needed):
   - Xcode
   - CodeRunner
   - OS X Server
   - Moom
   - PopClip
   - Alfred
   - Pages
   - Soulver
   - Evernote
   - Sketch
   - Skitch
   - Pixelmator
   - MultiMarkdown Composer
0. Open Xcode, accept the license agreement and download simulators and documentation. On a Terminal command line, execute `xcode-select --install` to install the command-line tools.
0. Install [Homebrew](http://brew.sh)
0. Open the Terminal application and run `java`. Download and install the JDK when prompted.
0. Download and install the [ADT Bundle](http://developer.android.com/sdk/index.html). *(Note: This is old; now Android Studio is the thing to download and install.)*
   - After installation, launch the Eclipse application. Choose the *Android SDK Manager* menu item, and install/update everything in these subtrees:
      - Tools
      - Android 4.3 (or whatever the newest API level is)
      - Extras
   - Choose *Help > Install New Software...*. Click the *Add...* button. Add this repository and install the Eclipse&nbsp;Color&nbsp;Theme plugin:
      - Name: Eclipse Color Theme Update Site
      - Location: `http://eclipse-color-theme.github.io/update/`
   - Download and install latest the HAXM driver from <https://software.intel.com/en-us/android/articles/intel-hardware-accelerated-execution-manager>. (If that link is broken, go to <https://software.intel.com/en-us/android/> and look for a HAXM download link.)
0. Set up `~/.bashrc` to run my shared scripts that are in `~/Dropbox/bin`.
0. Execute this in Terminal: `chflags nohidden ~/Library`
0. Set up ssh keys for [Bitbucket](https://confluence.atlassian.com/pages/viewpage.action?pageId=270827678) and [GitHub](https://help.github.com/articles/generating-ssh-keys).

Then to verify everything is ready to go, I use Git to grab the source code for an iOS app, and build it and run it, and then do the same for an Android app.

(For my Windows setup, see [Setting Up Windows, My Way](http://undefinedvalue.com/2013/12/22/setting-windows-my-way).)

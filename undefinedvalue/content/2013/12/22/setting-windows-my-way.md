Title: Setting Up Windows, My Way
Date: 2013-12-22 19:25:36
Category: Blog
Slug: setting-windows-my-way
Alias: 2013/12/22/setting-windows-my-way/
Tags: windows


This is a companion piece to my [Setting Up a New Mac, My Way](http://undefinedvalue.com/2013/08/30/setting-new-mac-my-way) entry. Thankfully, I haven't had to use Windows much in the past couple of years, but when I do have to set up a Windows machine for some task that requires it, I want to have a list of things to do to minimize the pain.

(This is a work in progress. It will evolve every time I go through the setup process, and every time I have to work around some annoying Windows limitation.)

1. Install/reinstall Windows. (The remaining steps assume the version is Windows 8.1 Pro x64, and it is running in VMWare on a Mac.)
1. In the Windows 8 start screen, remove everything except Desktop.
1. In Desktop, right-click the taskbar, choose Properties, select the Navigation tab, and check the *When I sign in or close all apps on a screen, go to the desktop instead of Start* box and the *Show the Apps view automatically when I go to Start* button.
1. In Settings (or Control Panel or wherever Microsoft puts these things this year) make these changes:
   - Ensure the Location is *United States* and *English (United States)* is the preferred language.
   - Enable automatic Windows updates.
   - Change the desktop background to a solid color.
   - Enable these desktop icons:
      - Computer
      - Network
      - Recycle Bin
   - Disable the screen saver and *Turn off the display* power option
   - Uncheck *Hide extensions for known file types*
   - Turn these Windows features on:
      - Internet Information Services (leave IIS 6 Management Compatibility off)
      - Telnet Client
1. Install these applications:
   - [Google Chrome](http://chrome.google.com/)
      - On first run, choose the *Relaunch Chrome on the desktop* menu item to get it as a window on the desktop
   - [Dropbox](https://www.dropbox.com/install)
   - [1Password](https://agilebits.com/onepassword/win)
   - [Sublime Text 3](http://www.sublimetext.com/3)
   - [Vim](http://www.vim.org/download.php)
   - [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
   - [Git](http://git-scm.com/download/win)
   - [Sourcetree](http://sourcetreeapp.com/)
   - [Beyond Compare](http://www.scootersoftware.com/download.php)
   - [Python 2.x](http://www.python.org/getit) and [NumPy](http://sourceforge.net/projects/numpy/files/)
      - Note: Unless you have a good reason, get the 32-bit version, not the 64-bit version. (It can be difficult to get 64-bit versions of third-party modules.)
   - [Node](http://nodejs.org/)
1. Start Powershell
   - Pin Powershell to the taskbar
   - Type this command to create the profile directory and file:<br>`new-item -path $profile -type file -force`
   - Type this command to copy my profile to this computer:<br>`cp ~/Dropbox/windows/powershell_profile.ps1 $profile`
   - Run Powershell as Administrator and run this command:<br>`set-executionpolicy -executionpolicy remotesigned`
   - Restart Powershell (with the new profile)
1. ... (to be continued) ...

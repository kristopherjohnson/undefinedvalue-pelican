Title: Havenjark Color Theme for Xcode 4
Date: 2012-10-30 11:59:34
Category: Blog
Slug: havenjark-color-theme-xcode-4
Alias: 2012/10/30/havenjark-color-theme-xcode-4/
Tags: xcode, havenjark, color


I've been experimenting with low-contrast color themes in my source-code editors. For a while, I thought I had settled on [Zenburn](http://slinky.imukuppi.org/zenburnpage/). However, I recently ran across [Havenjark](http://eclipsecolorthemes.org/?view=theme&id=25) in the Eclipse Color Themes plugin, and I decided it is perfection.

The only problem was that, while I could find Havenjark theme files for Eclipse and Textmate/Sublime Text 2, I could not find one for Xcode. So I converted the Eclipse color theme to Xcode 4's color theme format by hand.

If you'd like to try Havenjark in Xcode 4 yourself, download [Havenjark.dvtcolortheme](https://github.com/kristopherjohnson/havenjark/raw/master/Havenjark.dvtcolortheme) and copy it to your `~/Library/Developer/Xcode/UserData/FontAndColorThemes/` directory. Then, in Xcode, go to *Preferences* -> *Fonts & Colors* and select it.

My theme uses the Bitstream Vera Sans Mono font, which you can download for free from various locations on the Internet, or you can just change the font to something of your liking.

I'm not going to bother converting this to Visual Studio's color-theme format. There is no point in trying to make Windows development look nice.

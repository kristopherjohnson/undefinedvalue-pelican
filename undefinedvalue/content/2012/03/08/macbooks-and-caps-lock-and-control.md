Title: MacBooks and Caps Lock and Control
Date: 2012-03-08 23:46:44
Category: Blog
Slug: macbooks-and-caps-lock-and-control
Alias: 2012/03/08/macbooks-and-caps-lock-and-control/
Tags: rant, macbook, capslock


I learned to touch-type over 30 years ago, on an IBM Selectric typewriter. I'm a fast and accurate typist, compared to most programmers. I've always considered typing to be a basic skill that all programmers should take seriously. What goes on in your head is more important than how fast you can type, but the more efficient you are in getting your thoughts into the computer, the better you are going to be at your job.

I've been dismayed at one "feature" of my MacBook: to prevent accidental triggering of the Caps Lock key by incompetent typists, Apple makes it necessary to hold down the Caps Lock key for an extra fraction of a second. If you just tap it quickly, it does nothing. See http://support.apple.com/kb/HT1192 for Apple's explanation. They have also baked this behavior into some of their keyboards: see http://support.apple.com/kb/TS1578.

While I'm sure that many people welcome this feature, I do not. I type quickly and confidently, and my fingers hit the Caps Lock key at the appropriate times without me consciously thinking about it. I hit and release it so quickly that my MacBook ignores it. So when I type "UNIX is awesome!", "Party in the USA!" or "New York, NY", I see "unix is awesome!", "Party in the usa!" or "New York, ny" on the screen.

There is no easy way to disable this feature. When I complain, most people respond "Big deal. We hardly ever use Caps Lock." Well, I do. I've been using it for 30 years, and it has always worked fine. Until Apple decided It Should Just Not Work.

So, I looked into what I could do.
<!--break-->
The short answer is "Nothing". I have found a few mentions of kernel extensions and keyboard driver hacks, but this behavior seems to be embedded so deeply within OS X that there is no safe and reliable way to turn it off.

The cool kids all remap their Caps Lock key to work as the Control key. The reasoning is that programmers have to use the Control key a lot, and nobody has typed anything in all caps since 1968, so there is no need for a Caps Lock key. I have resisted doing any remapping of my keyboards, because I often have to use computers and keyboards that are not mine, and I didn't want to have to remember which keyboards are remapped and which are not. But since the Caps Lock key is useless to me, I decided to go ahead and give it a try.

This is easy to do on OS X: just go to *System Preferences* -> *Keyboard* and click the *Modifier Keys...* button, and then you can change the Caps Lock key to work as Control.

But then I don't have a Caps Lock key anymore, and I'd like to have one when I need to type "DANGER WILL ROBINSON! DANGER! DANGER! DANGER". Actually, joking aside, typing stuff in all caps comes up a lot in programming, and I've never understood why any programmers say they never need Caps Lock. Do they really hold down Shift while typing something like this?

    int fd = creat("file.dat", O_RDWR | O_CREAT | O_DSYNC | O_RSYNC);
    if (fd == -1) {
        if (errno == EEXIST) {
            /* ... */

I wanted to map some other key to Caps Lock for those times when I needed it. Some people swap their Caps Lock with Control, but I knew that wouldn't work for me: my fingers expect Control to be where it is, and I frequently use Control along with Command and/or Option, and hitting all those at once is awkward if the only Control key is where the Caps Lock key usually is.

What I really wanted to do was set things up so that double-tapping the Shift key would toggle Caps Lock mode, as it does on the virtual keyboards on iOS devices. I couldn't find a way to do that. So I decided I'd like to be able to hit Fn+Tab to trigger Caps Lock.

It turns out that can be done with the [KeyRemap4MacBook](http://pqrs.org/macosx/keyremap4macbook/) utility. It's a little hard to configure (especially if you aren't comfortable editing XML files), but I got it set up. If you want to play at home, here's what I did:

0. Download and install [KeyRemap4MacBook](http://pqrs.org/macosx/keyremap4macbook/). You'll have to restart at the end of the installation.
0. Open the **System Preferences** -> **KeyRemap4MacBook** preference pane.
0. Select the **Misc & Uninstall** tab, and click the **Open private.xml** button. This will open a Finder window in the folder where the `private.xml` configuration file is located.
0. Open `private.xml` in your favorite text editor (use TextEdit if you don't have a favorite text editor). It will be blank. Paste the following into it (which can also be found at https://gist.github.com/2002690 ):

<pre>
&lt;?xml version="1.0"?>
&lt;root>
  &lt;item>
    &lt;name>Private Settings&lt;/name>
    
    &lt;item>
      &lt;name>Fn+Tab to CapsLock&lt;/name>
      &lt;identifier>private.fn_tab_to_capslock&lt;/identifier>
      &lt;autogen>--KeyToKey-- KeyCode::TAB, ModifierFlag::FN, KeyCode::CAPSLOCK&lt;/autogen>
    &lt;/item>
    
  &lt;/item>
&lt;/root>
</pre>

Save the file, then go back to the **System Preferences -> KeyRemap4MacBook** preference pane and do this:

0. Select the **Change Key** tab.
0. Click the **ReloadXML** button to load your configuration file.
0. A **Private Settings** item should appear in the list in the preference pane. Expand the item, and check the **Fn+Tab to CapsLock** box.

Now, you should be able to press Fn+Tab, and you'll see the Caps Lock key light up.

I'm going to try this setup for a while, but I suspect I won't get used to it. Maybe I'll have to tweak it more, or maybe I'll just give up and learn to slow down for the Caps Lock key.

I've ordered a [Das Keyboard for Mac](http://www.daskeyboard.com/model-s-professional-for-mac/). Maybe that will be the ultimate solution to my problem.

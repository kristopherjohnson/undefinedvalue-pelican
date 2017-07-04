Title: Setting Up a Personal TiddlyWiki Server on OS X
Date: 2015-04-02 12:17:28
Category: Blog
Slug: setting-personal-tiddlywiki-server-os-x
Alias: 2015/04/02/setting-personal-tiddlywiki-server-os-x/
Tags: tiddlywiki


For a new job, I decided to set up a personal [wiki](http://en.wikipedia.org/wiki/Wiki) to keep notes. I wanted to keep it simple, meeting these requirements:

- All the data is in a Dropbox folder (so it can be automatically synced between machines)
- It must support [Markdown](http://daringfireball.net/projects/markdown/) syntax

After looking at the options, I settled on [TiddlyWiki](http://tiddlywiki.com). I've used "[classic TiddlyWiki](http://classic.tiddlywiki.com)" before, and liked its simplicity, but I was always a little annoyed with the weird steps you have to go through to save changes. The new version of TiddlyWiki ("TiddlyWiki5") includes support for running it as an HTTP server, so you can use it just like an online wiki.

But it took me a couple of hours to figure out how to set that up. The TiddlyWiki documentation is not clear ("not clear" is a euphemistic way of saying "terrible"). So I've written up these instructions in the hope it will spare somebody else all the frustration I had.

## Prerequisites

The following instructions assume you are using a Mac running OS X, and that you know how to use the Terminal to run commands and how to create and edit text files.

(If you're using Linux or BSD, you can probably figure out what you need to do differently. If you're running Windows, you have my sympathy.)

### Dropbox

Dropbox is not required to run TiddlyWiki, but I use it so that my personal notes will be available on all my machines.

If you don't already have Dropbox, go to <https://www.dropbox.com> to get started.

### Node

The TiddlyWiki server requires [Node](nodejs.org), so you will need to install that if you don't already have it.

If you are already using [Homebrew](http://brew.sh), then installation is as easy as this:

    brew install node

If you aren't using Homebrew, then go to <https://nodejs.org> and click the *Install* button.

### Time Machine

The first rule of using TiddlyWiki is **[back up your data](http://tiddlywiki.com/static/The%2520First%2520Rule%2520of%2520Using%2520TiddlyWiki.html)**. Using Dropbox serves as a rudimentary backup system, but it's not a real backup system.

If you haven't already set up Time Machine on your Mac, then go do it _right now_. See <https://support.apple.com/en-us/HT201250> for details.

## Installing TiddlyWiki

The TiddlyWiki server is available as an [NPM module](https://www.npmjs.com/package/tiddlywiki), so once you have Node installed, all you have to do is this:

    npm install -g tiddlywiki

You can do this to verify it is installed and usable:

    tiddlywiki --help

## Initializing Your Wiki Directory

You'll need to decide where to store your TiddlyWiki data. As I'm using Dropbox, I'll store everything in `/Users/kdj/Dropbox/tw`, but you can use whatever directory makes sense for you.

Run this command to initialize the directory for a TiddlyWiki server:

    tiddlywiki /Users/kdj/Dropbox/tw --init server

Note: you can run `tiddlywiki --editions` to see if any edition other than `server` might serve as a better starting point for you. I know that `server` works.

After running the above command, you should see that the specified directory contains a `tiddlywiki.info` file. This is the configuration file that controls how the server works.

## Enabling the Markdown Plugin

TiddlyWiki's [Markdown plugin](http://tiddlywiki.com/plugins/tiddlywiki/markdown/) is included with the distribution, but is not enabled by default. To enable it, you have to edit your `tiddlywiki.info` file and add `"tiddlywiki/markdown"` to the `plugins` section. When you have finished editing, the file should look like this:

    {
        "description": "Basic client-server edition",
        "plugins": [
            "tiddlywiki/tiddlyweb",
            "tiddlywiki/filesystem",
            "tiddlywiki/codemirror",
            "tiddlywiki/highlight",
            "tiddlywiki/markdown"
        ],
        "themes": [
            "tiddlywiki/vanilla",
            "tiddlywiki/snowwhite"
        ]
    }

## Running the Server

With everything set up, you can do this to run the server:

    tiddlywiki /Users/kdj/Dropbox/tw --server 19671

And then view it in a web browser: <http://localhost:19671>

Run `tiddlywiki --help server` to see what other options are available. You may want to use a different port, set a username/password, or otherwise customize the behavior.

## Starting the Server Automatically When You Log In

It would get annoying to have to type "`tiddlywiki /Users/kdj/Dropbox/tw --server 19671`" every time you wanted to use your personal wiki. Let's create a [launchd configuration file](https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man5/launchd.plist.5.html#//apple_ref/doc/man/5/launchd.plist) in the `~/Library/LaunchAgents` directory that will cause it to be automatically started every time we log in.

Go to your  `~/Library/LaunchAgents` directory and create a file named `com.tiddlywiki.plist` with the following contents, substituting the appropriate path for your data directory and the paths to the `node` and `tiddlywiki` executables. (Run `which node` and `which tiddlywiki` if you don't know what those paths are.)

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
      <key>Label</key>
      <string>com.tiddlywiki</string>
      <key>ProgramArguments</key>
      <array>
        <string>/usr/local/bin/node</string>
        <string>/usr/local/bin/tiddlywiki</string>
        <string>/Users/kdj/Dropbox/tw</string>
        <string>--server</string>
        <string>19671</string>
      </array>
      <key>EnvironmentVariables</key>
      <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
      </dict>
      <key>RunAtLoad</key>
      <true/>
      <key>WorkingDirectory</key>
      <string>/Users/kdj/Dropbox/tw</string>
      <key>StandardErrorPath</key>
      <string>error.log</string>
      <key>StandardOutputPath</key>
      <string>output.log</string>
    </dict>
    </plist>

After saving that file, log out and then log back in, and try to visit <http://localhost:19671>. If it works, great! If not, look for an `error.log` or `output.log` file in your data directory that may explain what went wrong.


## Restarting the Server

Unfortunately, using Dropbox to sync TiddlyWiki data between machines does not work as expected.  The TiddlyWiki server does not monitor changes to the filesystem, so even though Dropbox will copy changed files between machines, each TiddlyWiki instance just keeps displaying whatever data it read when it was launched.

So, after saving changes on one machine, we have to restart the TiddlyWiki server on the other machines to have those changes displayed everywhere.

The TiddlyWiki developers [may eventually fix this](http://tiddlywiki.narkive.com/npq5d9XI/tw-tiddlywiki-desktop-command-to-restart-node-instances), but in the meantime, we can define some shell commands to make it easy to restart the server when necessary.  Add these lines to your `~/.bashrc` file:

    export TWPLIST=~/Library/LaunchAgents/com.tiddlywiki.plist
    alias twstart="launchctl load $TWPLIST"
    alias twstop="launchctl unload $TWPLIST"
    alias twreload="twstop && sleep 1 && twstart && echo 'TiddlyWiki restarted'"

With these definitions, you can just execute `twreload` and refresh your browser whenever you sit down at one of your computers, and that local TiddlyWiki will refresh itself from Dropbox.


## Further Steps

Once you have everything working, explore the [TiddlyWiki](http://tiddlywiki.com) website to learn more about how to use it.

One of the first things you'll want to do is click the gear icon to go to the Control Panel and customize the site title and other settings.

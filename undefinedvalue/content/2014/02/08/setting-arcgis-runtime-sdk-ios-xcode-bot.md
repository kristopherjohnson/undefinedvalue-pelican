Title: Setting Up ArcGIS Runtime SDK for iOS for Xcode Bot
Date: 2014-02-08 16:48:55
Category: Blog
Slug: setting-arcgis-runtime-sdk-ios-xcode-bot
Alias: 2014/02/08/setting-arcgis-runtime-sdk-ios-xcode-bot/
Tags: xcode, iosdev, bot, arcgis


I am working on an iPad app that uses the [ArcGIS Runtime SDK for iOS](https://developers.arcgis.com/ios/). Esri provides an easy-to-use installer and [instructions](https://developers.arcgis.com/ios/info/install.htm) for setting up the SDK so that it can be used with Xcode.

The installer puts the SDK files in the user’s home directory, and the setup guide recommends using paths like `$(HOME)/Library/SDKs/ArcGIS/iOS/` in Xcode projects to find the framework’s headers and libraries. This works fine as long as one is using Xcode as a user who has installed the SDK. However, it causes problems if one wants to set up an [Xcode bot](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/xcode_guide-continuous_integration/ConfigureBots/ConfigureBots.html) to automatically build and test the app. The Xcode service that runs bots executes under the `_teamsserver` user account, and by default that user’s home directory does not exist, and you can’t log in as that user to run the SDK installer. So attempts to create a bot to build the app just result in “ArcGIS.h not found” compilation errors.

After I bit of Googling and experimentation, I came up with a solution:

0. Install the SDK in my user account (or another normal account), following Esri’s installer and instructions.
0. Make my `~/Library` directory world-readable:<br>`chmod 755 ~/Library`
0. Create the `/var/teamsserver` home directory for the `_teamsserver` user:<br>`sudo mkdir /var/teamsserver`
0. Create the `/var/teamsserver/Library` directory for the `_teamsserver` user:<br>`sudo mkdir /var/teamsserver/Library`
0. Set `_teamsserver` as the owner of the directories:<br>`sudo chown -R _teamsserver:_teamsserver /var/teamsserver/`
0. Set permissions on the directories:<br>`sudo chmod -R 770 /var/teamsserver/`
0. Create a symbolic link to the SDK installation:<br>`sudo ln -s ~/Library/SDKs /var/teamsserver/Library/SDKs`

This works. It could be argued that it would be better to set up the symbolic links in some shared location (`/Library`, `/usr/local`, etc.) and then use a full path in the Xcode project to find them, but I prefer this solution because it doesn’t require any extra steps for developers who don’t need to set up a bot.


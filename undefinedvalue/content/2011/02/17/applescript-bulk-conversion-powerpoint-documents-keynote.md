Title: AppleScript for Bulk Conversion of PowerPoint Documents to Keynote
Date: 2011-02-18 01:47:43
Category: Blog
Slug: applescript-bulk-conversion-powerpoint-documents-keynote
Alias: 2011/02/17/applescript-bulk-conversion-powerpoint-documents-keynote/
Tags: powerpoint, keynote, applescript


The instructor in one of my MBA-prerequisite classes distributed a set of PowerPoint presentations as course notes. I want to review these on my iPad, so I needed to convert them to Keynote.

This is pretty easy to do manually on a Mac: Just right-click the PPT file, select **Open With... -> Keynote** from the menu (which reads the PowerPoint file into Keynote), then **File -> Save As...** to store it where you want it. However, I am a programmer, so I would rather spend a few hours figuring out how to write a program to do a repetitive task than simply spend the five minutes needed to do it by hand.

At first I tried using Apple's Automator utility, which is supposed to make stuff like this easy, but I couldn't figure it out. So, I took the plunge into AppleScript.

As with every foray I make into AppleScriptLand, I was frustrated, annoyed, saddened, and exhausted by the experience. But I did succeed (if two hours spent futzing with AppleScript can possibly be called a _success_).

So, if you have need for a utility for converting a bunch of PowerPoint files to Keynote, open up the AppleScript Editor and copy and paste this script into the window:

    on open droppedFiles
        set theDestinationFolder to (choose folder with prompt "Choose destination folder") as Unicode text
        repeat with theFile in droppedFiles
            tell application "Keynote"
                open theFile
                set theSlideshow to slideshow 1
                set theDestinationPath to theDestinationFolder & (name of theSlideshow)
                save theSlideshow in theDestinationPath
                close theSlideshow
            end tell
        end repeat
    end open

Click the **Compile** button, and assuming you see no errors, choose **File -> Save**, set the File Format to **Application**, and save it to the desired place with the desired name.

Then, to convert files, just select them in the Finder and drag them onto the application icon. You will be prompted for a destination folder, then the script will do its thing.

The script looks pretty simple and straightforward, right? Well, AppleScript is a language that is easy to read, but very, very difficult to write. Every programming language that tries to "look like plain English" is a nightmare to use, because like English, the rules are illogical, arbitrary, and self-contradictory. Every application, like Keynote, has its own commands and object types, and the documentation is poor, so you end up doing a lot of experimentation and hair-pulling. The hardest part of this particular script was figuring out that I needed to add the `as Unicode text` conversion in order to produce a valid file path.

(This article is based upon my question and answer in the [Ask Different](http://apple.stackexchange.com/questions/8317/applescript-or-automator-workflow-for-bulk-converting-powerpoint-presentations-to) Q&A forum.)

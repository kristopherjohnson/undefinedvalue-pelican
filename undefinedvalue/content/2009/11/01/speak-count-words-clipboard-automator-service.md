Title: "Speak Count of Words on Clipboard" Automator Service
Date: 2009-11-01 23:43:35
Category: Blog
Slug: speak-count-words-clipboard-automator-service
Alias: 2009/11/01/speak-count-words-clipboard-automator-service/
Tags: snowleopard, osx, mac, automator


As part of my ["write a blog entry every day during November"](http://undefinedvalue.com/2009/11/01/not-quite-nanowrimo) commitment, I considered imposing a minimum word limit for each entry.  I've decided against that, because I don't want to feel pressure to add filler, but before deciding that, I created an Automator service that would help me to count words.
<!--break-->
## How to Use the Service

To use it, just select some text, hit Command-C to copy it to the clipboard, and then choose **Speak Count of Words on Clipboard** from the application's **Services** menu. 

## How to Create It

Here's how to create the service (using Mac OS X 10.6 Snow Leopard, of course):

0. Start Automator, and choose "Service" as the workflow template.
0. Choose "no input" and "any application" in the "Service receives . . ." section at the top.
0. Drag a **Get Contents of Clipboard** action from the left column to the workflow pane.
0. Drag a **Run Shell Script** action from the left column to the workflow pane, beneath the **Get Contents of Clipboard** action.
0. In the **Run Shell Script** text area, replace "cat" with this:<pre>
echo "The selection contains &#96;wc -w&#96; words."</pre>
0. Drag a **Speak Text** action from the left column into the workflow area, beneath the **Run Shell Script** action.
0. Choose the **File -> Save** menu item, and save it as "Speak Count of Words on Clipboard".

Here's how it should look:

<img src="http://undefinedvalue.com/sites/undefinedvalue.com/files/Speak_Count_of_Words_on_Clipboard_service.png" alt="Picture">

If you think you are going to use this a lot, go to the Services Preferences and assign a keyboard shortcut.

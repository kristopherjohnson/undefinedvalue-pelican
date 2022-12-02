Title: Automator Service: Copy File Paths to Clipboard
Date: 2009-11-05 09:12:31
Category: Blog
Slug: automator-service-copy-file-paths-clipboard
Alias: 2009/11/05/automator-service-copy-file-paths-clipboard/
Tags: snowleopard, automator


Here's another Snow Leopard Automator-based service: It takes the Finder selection and puts the file paths on the clipboard, for easy pasting into command lines or scripts.
<!--break-->
## How to Use It

0. In the Finder, select one or more files or folders.
0. From the Services menu, select **Copy Files Paths to Clipboard**
0. Go somewhere and select **Edit -> Paste** to put the full path(s) to the file(s) there.

For example, if I go to my home folder, select the "Documents" and "Downloads" folders, and then invoke the service, this is what ends up on the clipboard:

    /Users/kdj/Documents
    /Users/kdj/Downloads


## How to Make It

Open Automator, create a new Service, and set it to receive selected files or folders in the Finder.

Add these actions:

0. **Run Shell Script**, with shell `/bin/bash`, passing input **as arguments**, with this script:<pre><code>
    for f in "$@"
    do
        echo "$f"
    done
</code></pre>
0. **Copy to Clipboard**

Save it, and name it "Copy File Paths to Clipboard".

<img src="https://undefinedvalue.com/sites/undefinedvalue.com/files/Copy_File_Paths_to_Clipboard.png" alt="Picture">

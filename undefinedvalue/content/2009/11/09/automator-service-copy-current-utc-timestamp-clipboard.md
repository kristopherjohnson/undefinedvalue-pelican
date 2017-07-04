Title: Automator Service: Copy Current UTC Timestamp to Clipboard
Date: 2009-11-10 00:12:31
Category: Blog
Slug: automator-service-copy-current-utc-timestamp-clipboard
Alias: 2009/11/09/automator-service-copy-current-utc-timestamp-clipboard/
Tags: automator


Yeah, I know, you're probably getting sick of these Automator services. But I really do create a new one of these practically every day to make my life a little easier, and maybe some of these will be useful to others.

This one puts a UTC timestamp on the clipboard. The timestamp is an [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)-format string like "2009-11-09T13:14:03Z". If you'd like a different format, type "man date" in Terminal to see how to change the output format of the `date` command in the shell script below.
<!--break-->
## How to Use It

Choose **Copy Current UTC Timestamp to Clipboard** from the Services menu, then paste it into wherever you need it.

## How to Make it

0. Start up Automator, and create a new Service which takes **no input** in **any application**
0. Add a **Run Shell Script** action, with shell **/bin/bash** and which passes input **to stdin**. Replace the shell script text with this:<pre>
<br>/bin/date -u '+%FT%TZ'<br></pre>
0. Add a **Copy to Clipboard** action.
0. Choose **File -> Save** and name it "Copy Current UTC Timestamp to Clipboard"

<img src="http://undefinedvalue.com/sites/undefinedvalue.com/files/Copy_UTC_Timestamp_to_Clipboard.png" alt="Screenshot">

Title: An OS X Automator Service for Reformatting JSON Text
Date: 2013-03-01 16:35:11
Category: Blog
Slug: os-x-automator-service-reformatting-json-text
Alias: 2013/03/01/os-x-automator-service-reformatting-json-text/
Tags: node, json, automator


**Note: This is an old post. I now use jq (<http://stedolan.github.io/jq/>) instead of the `formatjson` Node script described below, and I recommend that you do too.**

I had some JSON files that were not indented consistently. I edit these files by hand, so I wanted a way to easily reformat them.

My text editor has a reformatting command, but I really hate what it produces, so I decided to make my own JSON reformatting service for OS X that I could use in any application.
<!--break-->
First, I wrote a [Node.js](http://nodejs.org) script to do the reformatting:

<script src="https://gist.github.com/kristopherjohnson/5065599.js"></script>

(Also available as [Literate CoffeeScript](http://gist.github.com/kristopherjohnson/5153772)).

I saved that file as `~/bin/formatjson`, and made it executable with `chmod +x ~/bin/formatjson`.

Then I used Automator to create a service:

0. Launch Automator
0. Create a new Automator document of type *Service*
0. Set it to "Service receives selected **text** in **any application**", and check the **Output replaces selection text** box.
0. Drag a *Run Shell Script* action into the workflow, and enter the following command:
   - `PATH=$PATH:~/bin:/usr/local/bin formatjson`
0. Save the service with the name "Reformat JSON Text".

(Note: In step 4, if your `node` executable is not in `/usr/local/bin`, then substitute the appropriate directory. Also, if you saved `formatjson` to a directory other than `~/bin`, substitute the appropriate directory for that.)

<img src="https://s3.amazonaws.com/undefinedvalue/ReformatJSONTextService.png" height="413" width="600" alt="Automator screenshot"/>

Now, whenever I want to reformat some JSON in a text editor, I just select it, right-click, and choose **Services&nbsp;>&nbsp;Reformat&nbsp;JSON&nbsp;Text**.

And when I want to reformat things from the command line, this works:

    formatjson <ugly.json >pretty.json

If you'd rather have a web page that does this, see [A Web Page for Reformatting JSON Text](https://undefinedvalue.com/2013/03/02/web-page-reformatting-json-text).

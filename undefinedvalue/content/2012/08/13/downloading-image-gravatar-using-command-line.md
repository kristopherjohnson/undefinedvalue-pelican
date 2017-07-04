Title: Downloading an Image from Gravatar Using the Command Line
Date: 2012-08-13 20:28:08
Category: Blog
Slug: downloading-image-gravatar-using-command-line
Alias: 2012/08/13/downloading-image-gravatar-using-command-line/
Tags: shell, gravatar, bash


I am signed up for the [app.net](join.app.net) alpha, and wanted to upload my avatar picture. Unfortunately, I can't find my avatar picture anywhere on my computer.

[Gravatar](http://gravatar.com) is a free service that allows you to save your avatar (picture) for use by multiple websites. Gravatar has a copy of the avatar I wanted, so I hoped I could just download it via the same user interface you use to upload images. It turns out that you can't do that: the user interface lets you upload pictures, but does not provide a download option. So I had to figure out how to retrieve my image the way that a Gravatar web client would.

According to the [Gravatar documentation](http://en.gravatar.com/site/implement/images/), one can get a image for a user by doing an HTTP GET with a URL of this form:

    http://www.gravatar.com/avatar/HASH

where `HASH` is the MD5 hash of the user's email address. You can calculate this using the [md5](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/md5.1.html) command-line utility.

So, here is the complete command line that will calculate my MD5 hash and the retrieve the image using the [curl](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/curl.1.html) utility:

<script src="https://gist.github.com/3343852.js?file=gravatar.sh"></script>

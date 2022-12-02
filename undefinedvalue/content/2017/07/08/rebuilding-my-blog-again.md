Title: Rebuilding My Blog Again, with Pelican
Date: 2017-07-08 15:00:00
Category: Blog
Slug: rebuilding-my-blog-again
Tags: blog, drupal, mysql, pelican, python

I've moved this blog from a [Drupal](https://www.drupal.org) CMS running on an AWS EC2 instance to a statically generated set of pages hosted on [GitHub Pages](https://pages.github.com).  If you're curious about the reasons and the process, read on.

For several years, my blog has been running on Drupal 6.  Drupal [seemed like a good idea when I started](https://undefinedvalue.com/2009/04/18/drupal-rocks), as it was a mature easy-to-use content management system, but I've been wanting to get away from it for a while.  I spend more time maintaining Drupal then I do writing articles for the blog.  When I started I had to do [a lot of work](https://undefinedvalue.com/2010/11/12/setting-drupal-6-ubuntu-1010-ec2) to get Drupal configured and running well.  There are always new versions and security updates to apply, and I really should have upgraded to Drupal 7 and then Drupal 8 somewhere along the way, but I haven't and now I can't update to newer versions of Ubuntu. The care and feeding of Drupal is too much work for the benefits it provides for my simple blog.

I decided to move to a static site generator, as I don't need dynamic features and I want to avoid the pain of setting up any more CMSes or blogging engines on any server.

My basic requirements for the new generator were these:

- Provide a similar front page layout, with a list of ten "teasers" from most recent entries, a list of archives, an "About" page, and a few links to other stuff.
- Support existing URLs for existing pages (so old links will work).
- Support tags.
- Be able to run the generator on my laptop and easily upload the generated static pages to my Apache web server, or S3, or GitHub Pages.
- Let me write posts in [Markdown](https://daringfireball.net/projects/markdown/syntax) format.


The Drupal 6 Database
---------------------

My first step was to export the existing articles and metadata from the Drupal database on my blog server, and recreate it on my development machine.  Looking at my Drupal configuration, I was able to find the database name and login information (which I forgot years ago).  I used `mysqldump` to export the data.

    :::bash
    mysqldump --user=$dbuser --password=$dbpass --tz-utc --databases "drupal6_undefinedvalue" > "drupal6_undefinedvalue.sql"

Then, after copying the file to my dev machine, I loaded it with the MySQL command `source drupal6_undefinedvalue.sql`.

Rather than reading Drupal source code or documentation, I just used a lot of MySQL "show tables", "describe", and `SELECT` commands to figure out the database schema.  These are the tables and columns that I found useful:

- `node`: metadata about all the Drupal "nodes", or pages
    - `nid`: node ID (primary key)
    - `type`: `book`, `page`, or `story`.  My blog posts are all of type `story`.
    - `title`: the original title of the post
    - `status`: 0 for an unpublished post, or 1 for a published post.
    - `created` and `changed`: timestamps
- `node_revisions`: the content of each node
    - `nid`: node ID
    - `title`: current title
    - `body`: main content
    - `timestamp`
    - `format`: foreign key into the `filter_formats` table
- `filter_formats`: list of filter formats for posts
    - `format`: key
    - `name`: "Filtered HTML", "Full HTML", "Filtered Markdown", or "Full Markdown"
- `term_node`: association of posts with tags
- `term_data`: tags
- `url_alias`: provides mappings from URLs like "node/288" to "2017/04/22/my-first-chess-program"

The `body` of a `node_revisions` record contains a special token `<!--break-->` between the "teaser" portion and the rest.

I wrote a Python script that could extract the relevant fields from these tables and print out the attributes I expected to see.  If you want to see it, check out [my drupal6tostatic repository](https://github.com/kristopherjohnson/drupal6tostatic).


Static Site Generators
----------------------

The next step was to decide on a static site generator.

A "static site generator" (SSG) is a program that, given a bunch of input files and templates and configuration files and code, will generate a tree of static HTML pages that can be uploaded to a web server.

I briefly thought about writing my own SSG, but my goal here was to get my blog moved as quickly and painlessly as possible, so I decided to go with an off-the-shelf solution.  The most popular SSG is currently [Jekyll](https://jekyllrb.com), but I don't like Ruby much and would prefer a Python&nbsp;3-based tool.  After a brief survey of the available Python SSGs, I decided to give these a try:

- [Cactus](https://github.com/eudicots/Cactus)
- [Hyde](http://hyde.github.io)
- [Pelican](http://getpelican.com)

Cactus didn't work with Python&nbsp;3. It almost worked, but the blog plugin wasn't compatible with Python&nbsp;3, and after I fixed that, it generated an empty index page.  With Python 2, it worked, but its blog plugin didn't support the directory hierarchy I wanted to maintain.  Rather than fix these issues, I moved on to the next candidate.

Hyde didn't support Python&nbsp;3. (The website says Python&nbsp;3 support is "in progress".)  I gave it a try anyway, and while I didn't hate it, I really want something that works with Python&nbsp;3 and doesn't require a lot of configuration.  (For every YAML file I see, I expect at least one hour of messing around with it.)

Pelican worked pretty well on my first try (except for a CRITICAL error when running `pelican generate` with a not-well-formed Markdown file) and it seemed to be the most well-documented and well-supported of the generators I tried.  Out-of-the-box, it handled pagination and other desirable features that would have required configuration or additional coding in Cactus or Hyde.

So I decided to use Pelican as my site generator.


Python 3 Virtual Environment
----------------------------

To ensure I'd be able to easily run the Pelican generator on any machine, now or in the future, I set up a Python&nbsp;3 [virtual environment](https://docs.python.org/3.5/library/venv.html) and installed the necessary packages:

    python3 -m venv-pelican-blog                # create the environment
    source venv-pelican-blog/bin/activate       # activate the environment
    pip install pelican pelican-alias markdown  # install dependencies

And then before running any Pelican commands, I have to make sure I run the command `source venv-pelican-blog/bin/activate`.


Configuring Pelican
-------------------

To support automatic redirects from old URLs to the new pages, I installed the [pelican-alias](https://github.com/Nitron/pelican-alias) plugin, and updated my generator script so that it would include an `Alias:` item for each old article.

I added an `about-me.md` file to the `content/pages` subdirectory, so that would also appear at the top of the page as it does in the Drupal site.

I set the `LINKS` and `SOCIAL` settings in `pelicanconf.py` so that I would get lists of links similar to what was in the Drupal blog's "blocks".

I set the `YEAR_ARCHIVE_SAVE_AS`, `MONTH_ARCHIVE_SAVE_AS`, and `DAY_ARCHIVE_SAVE_AS` variables in `pelicanconf.py` to generate archive pages with paths identical to what was used in Drupal.


Theme and Styles
----------------

Finally, I wanted a theme similar to that of the [WhiteJazz](https://www.drupal.org/project/whitejazz) theme I had used with Drupal 6.  Pelican comes with two built-in themes: `simple`, which is just plain text with no styling, and `notmyidea`, which is what the [getpelican.com](http://getpelican.com) website uses.  Rather than perusing all the other themes available for Pelican, I decided to try to replicate WhiteJazz myself, with the expectatation that I would give up in frustruation after a few hours and look for an off-the-shelf theme.

Thankfully, it turned out to be easier than I expected to create my own theme.  I started by copying the `simple` theme files to a new directory, then updated the templates that didn't quite do what I wanted, and added some CSS.  For the basic CSS, I chose [Skeleton](http://getskeleton.com), a simple CSS framework which I had used before in my [What's Good on TCM?](http://secretspacelab.com/tcm.html) site.  It was easy to set up its grid to provide the basic layout of WhiteJazz.  I then added my own CSS rules and template customizations, borrowing liberally from the WhiteJazz CSS and notmyidea templates, until I had what I wanted.

One problem I ran into was that the `simple` framework had an empty (0 bytes) `tag.html` template, and was missing other files related to tags.  So I copied the missing files from `notmyidea`.


Publishing the New Site
-----------------------

I had already set up my personal `kristopherjohnson.github.io` repo as a GitHub Pages site.  I set up a Makefile rule that would copy the output from Pelican to that local repo, commit the change, and then push that repo to GitHub.

So, all I have to do to regenerate the site and push it to the cloud is this:

    cd ~/work/undefinedvalue-pelican
    source venv-pelican-blog/bin/activate
    make github

It takes about four seconds to run `make github`.  After that, it takes a minute or so before the changes are actually visible on the site.

Finally, I went to my domain registrar and updated the `undefinedvalue.com` address records so it now points to GitHub rather than to my old server, following the instructions on these pages:

- [Quick start: Setting up a custom domain](https://help.github.com/articles/quick-start-setting-up-a-custom-domain/)
- [Setting up an apex domain](https://help.github.com/articles/setting-up-an-apex-domain/)


Conclusion
----------

I've wanted to do this migration for over a year, but feared it would take up a few weekends and be full of frustration.  It was actually a lot easier than I expected.  The hardest part for me was getting the CSS right.  It feels good that I figured out how to do a full conversion by writing a few scripts and modifying some configuration files and templates.

One thing I miss is the simplicity of editing with Drupal.  If I saw a typo on the site, I could just click an _Edit_ button, fix it, and _Save_.  Now if I see something wrong, I have to find the right input file in my tree of files, edit it, and then republish, and then wait a minute to see if it looks right.  But I am very happy to no longer be dependent upon a MySQL database, an old version of a PHP-based CMS, and an EC2 web server.

If you want to see my Pelican setup, it's available here for all to see: <https://github.com/kristopherjohnson/undefinedvalue-pelican>.


undefinedvalue-pelican
----------------------

This is the [Pelican](http://docs.getpelican.com/en/stable/) project I use to build the static pages for my [Undefined Value](http://undefinedvalue.com/) blog.

First, run this command to enable the virtual Python 3 environment that has Pelican and other dependencies installed:

    source venv-pelican/bin/activate

To create a new post:

    make newpost

To regenerate and publish the site to GitHub Pages:

    make github

Use `make help`, or `make` with no arguments to see other targets.

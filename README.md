undefinedvalue-pelican
----------------------

This is the [Pelican](http://docs.getpelican.com/en/stable/) project I use to build the static pages for my [Undefined Value](http://undefinedvalue.com/) blog.

First, run this command to enable the virtual Python 3 environment that has Pelican and other dependencies installed:

    source venv-pelican/bin/activate

(If you can't or won't use the virtual environment, you need to `pip install pelican pelican-alias markdown`.)

To create a new post:

    make newpost

To regenerate and publish the site to GitHub Pages:

    make github

Note that `make github` assumes that you have the <https://github.com/kristopherjohnson/kristopherjohnson.github.io> repo cloned to `~/work/kristopherjohnson.github.io`.

Use `make help`, or `make` with no arguments to see other targets.

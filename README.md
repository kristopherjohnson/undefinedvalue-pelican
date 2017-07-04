undefinedvalue-pelican
----------------------

This is the [Pelican](http://docs.getpelican.com/en/stable/) project I use to build the static pages for my [Undefined Value](http://undefinedvalue.com/) blog.

First, run this command to enable the virtual Python 3 environment that has Pelican and other dependencies installed:

    source venv-pelican/bin/activate

Then, to build the pages in the `undefinedvalue/output` directory:

    make html

Use `make help`, or `make` with no arguments to see other targets.

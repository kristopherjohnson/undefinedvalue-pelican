#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristopher Johnson'
SITENAME = 'Undefined Value'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Per-month archive
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}{date:%m}/index.html'

# Blogroll
LINKS = (("Kris's Résumé", 'http://undefinedvalue.com/page/kjresume'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/OldManKris'),
          ('GitHub', 'https://github.com/kristopherjohnson'),
          ('Stack Overflow', 'http://stackoverflow.com/users/1175/kristopher-johnson'),
          ('LinkedIn', 'http://www.linkedin.com/in/kristopherdjohnson'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['pelican_alias']

THEME = '../themes/undefinedvalue'


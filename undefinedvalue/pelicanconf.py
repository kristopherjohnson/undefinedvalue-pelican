#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristopher Johnson'
SITENAME = 'Undefined Value'
SITESUBTITLE = "Kris Johnson's Blog"
SITEURL = ''
COPYRIGHT_NOTICE = '© 2003-2017 Kristopher Johnson'

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
YEAR_ARCHIVE_SAVE_AS = 'archive/{date:%Y}/index.html'

# Per-month archive
MONTH_ARCHIVE_SAVE_AS = 'archive/{date:%Y}{date:%m}/index.html'

# Per-day archive
DAY_ARCHIVE_SAVE_AS = 'archive/{date:%y}{date:%m}{date:%d}/index.html'

# Top-banner items
MENUITEMS = (('Front Page', '/'),
             ('Tags', '/tags.html'),
             ('Archives', '/archives.html'))

# External links
LINKS = (("What's Good on TCM?", 'http://secretspacelab.com/tcm.html'),
         ('GitHub', 'https://github.com/kristopherjohnson'),
         ('Bitbucket', 'https://bitbucket.org/KristopherJohnson/'))
LINKS_WIDGET_NAME = 'Other Stuff'

# Social networks
SOCIAL = (('Twitter', 'http://twitter.com/OldManKris'),
          ('Stack Overflow', 'http://stackoverflow.com/users/1175/kristopher-johnson'),
          ('Pinboard', 'https://pinboard.in/u:OldManKris'),
          ('Flickr', 'https://www.flickr.com/photos/kristopherjohnson/'),
          ('LinkedIn', 'http://www.linkedin.com/in/kristopherdjohnson'),)
SOCIAL_WIDGET_NAME = 'More of Me'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = ['pelican_alias']

THEME = '../themes/undefinedvalue'

STATIC_PATHS = ['files']


#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristopher Johnson'
SITENAME = 'Undefined Value'
SITESUBTITLE = "Kris Johnson's Blog"
SITEURL = ''
COPYRIGHT_NOTICE = '© 2003-2023 Kristopher Johnson'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = 'en'

DEFAULT_DATE_FORMAT = '%Y-%m-%d'

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
DAY_ARCHIVE_SAVE_AS = 'archive/{date:%Y}{date:%m}{date:%d}/index.html'

# Top-banner items
MENUITEMS = (('Front Page', '/'),
             ('Tags', '/tags.html'),
             ('Archives', '/archives.html'))

# Recent Posts
RECENT_ARTICLES_WIDGET_NAME = 'Recent Posts'
RECENT_ARTICLES_COUNT = 5

# External links
LINKS = (("What's Good on TCM?", 'http://secretspacelab.com/tcm.html'),
         ('GitHub', 'https://github.com/kristopherjohnson'),
         ('Bitbucket', 'https://bitbucket.org/KristopherJohnson/'))
LINKS_WIDGET_NAME = 'Other Stuff'

# Social networks
SOCIAL = (('Mastodon', 'https://mastodon.xyz/@oldmankris'),
          ('Stack Overflow', 'http://stackoverflow.com/users/1175/kristopher-johnson'),
          ('LinkedIn', 'http://www.linkedin.com/in/kristopherdjohnson'),
          ('Flickr', 'https://www.flickr.com/photos/kristopherjohnson/'),
          ('Twitter', 'http://twitter.com/OldManKris'))
SOCIAL_WIDGET_NAME = 'Follow'

DISPLAY_SEARCH_ON_MENU = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

PLUGIN_PATHS = ['../plugins', '../pelican-plugins']
PLUGINS = ['age_in_days', 'pelican_alias', 'neighbors', 'sitemap']

THEME = '../themes/undefinedvalue'

SITEMAP = {
    'format': 'xml'
}

STATIC_PATHS = ['files']

EXTRA_PATH_METADATA = {
    'files/robots.txt': { 'path': 'robots.txt' },
    'files/CellGradientBackground.png':
        { 'path': 'sites/undefinedvalue.com/files/CellGradientBackground.png' },
    'files/Copy_File_Paths_to_Clipboard.png':
        { 'path': 'sites/undefinedvalue.com/files/Copy_File_Paths_to_Clipboard.png' },
    'files/Copy_UTC_Timestamp_to_Clipboard.png':
        { 'path': 'sites/undefinedvalue.com/files/Copy_UTC_Timestamp_to_Clipboard.png' },
    'files/GradientButtonsAppScreenshot.png':
        { 'path': 'sites/undefinedvalue.com/files/GradientButtonsAppScreenshot.png' },
    'files/GradientButtonsInterfaceBuilder.png':
        { 'path': 'sites/undefinedvalue.com/files/GradientButtonsInterfaceBuilder.png' },
    'files/GradientTableViewCell.h':
        { 'path': 'sites/undefinedvalue.com/files/GradientTableViewCell.h' },
    'files/GradientTableViewCell.m':
        { 'path': 'sites/undefinedvalue.com/files/GradientTableViewCell.m' },
    'files/HourglassIcon256x256.png':
        { 'path': 'sites/undefinedvalue.com/files/HourglassIcon256x256.png' },
    'files/MenuTimerIcon256x256.png':
        { 'path': 'sites/undefinedvalue.com/files/MenuTimerIcon256x256.png' },
    'files/NewHourglassIcon256x256.png':
        { 'path': 'sites/undefinedvalue.com/files/NewHourglassIcon256x256.png' },
    'files/NoGradient.png':
        { 'path': 'sites/undefinedvalue.com/files/NoGradient.png' },
    'files/Scale_Images_by_75_percent.png':
        { 'path': 'sites/undefinedvalue.com/files/Scale_Images_by_75_percent.png' },
    'files/Speak_Count_of_Words_on_Clipboard_service.png':
        { 'path': 'sites/undefinedvalue.com/files/Speak_Count_of_Words_on_Clipboard_service.png' },
    'files/Tiles_Screenshot.png':
        { 'path': 'sites/undefinedvalue.com/files/Tiles_Screenshot.png' },
    'files/WithGradient.png':
        { 'path': 'sites/undefinedvalue.com/files/WithGradient.png' },
    'files/calculator.js_.txt':
        { 'path': 'sites/undefinedvalue.com/files/calculator.js_.txt' },
    'files/calculator_tests.html_.txt':
        { 'path': 'sites/undefinedvalue.com/files/calculator_tests.html_.txt' },
    'files/calculator_tests.js_.txt':
        { 'path': 'sites/undefinedvalue.com/files/calculator_tests.js_.txt' },
    'files/iStock_000001485226XSmall.jpg':
        { 'path': 'sites/undefinedvalue.com/files/iStock_000001485226XSmall.jpg' },
    'files/iStock_000002585519XSmall.jpg':
        { 'path': 'sites/undefinedvalue.com/files/iStock_000002585519XSmall.jpg' },
    'files/jb-screenshot-small.png':
        { 'path': 'sites/undefinedvalue.com/files/jb-screenshot-small.png' },
    'files/temperaturewarning.png':
        { 'path': 'sites/undefinedvalue.com/files/temperaturewarning.png' },
}

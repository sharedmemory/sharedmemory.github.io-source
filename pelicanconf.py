#/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = u'Carey Chou'
SITENAME = u'Shared Memory'
SITEURL = ''  # http://sharedmemory.github.io'

#PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

MARKUP = ('md')

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']

THEME = './clean-blog-theme'
STATIC_PATHS = ['images']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = PAGE_SAVE_AS

STATIC_PATHS = ['images', 'CNAME', 'favicon.ico', 'robots.txt']

DEFAULT_HEADER_BG = '/images/buddhabrot.png'
HEADER_COVER = '/images/buddhabrot.png'
ABOUT_PAGE = '/pages/about.html'
SHOW_ARCHIVES = True
SHOW_FEED = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'render_math', 'liquid_tags', 'pelican_comment_system']

PELICAN_COMMENT_SYSTEM = True
PELICAN_COMMENT_SYSTEM_DIR = '../comments'

SITEMAP = {
    'format': 'xml',
}

# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings as django_settings
from django.utils.translation import ugettext_lazy as _


OBJECT_TYPES = (
    ('Article', _('Article')),
    ('Website', _('Website')),
)
TWITTER_TYPES = (
    ('summary', _('Summary Card')),
    ('summary_large_image', _('Summary Card with Large Image')),
    ('app', _('App Card')),
)
FB_TYPES = OBJECT_TYPES
GPLUS_TYPES = (
    ('Article', _('Article')),
    ('Blog', _('Blog')),
    ('WebPage', _('Page')),
    ('WebSite', _('WebSite')),
    ('Event', _('Event')),
    ('Product', _('Product')),
    ('Place', _('Place')),
    ('Person', _('Person')),
)


DEFAULT_IMAGE = getattr(django_settings, 'META_DEFAULT_IMAGE', False)
DEFAULT_TYPE = getattr(django_settings, 'META_SITE_TYPE', False)
FB_TYPE = getattr(django_settings, 'META_FB_TYPE', False)
FB_TYPES = getattr(django_settings, 'META_FB_TYPES', FB_TYPES)
FB_APPID = getattr(django_settings, 'META_FB_APPID', False)
FB_PROFILE_ID = getattr(django_settings, 'META_FB_PROFILE_ID', False)
FB_PUBLISHER = getattr(django_settings, 'META_FB_PUBLISHER', False)
FB_AUTHOR_URL = getattr(django_settings, 'META_FB_AUTHOR_URL', False)
TWITTER_TYPE = getattr(django_settings, 'META_TWITTER_TYPE', False)
TWITTER_TYPES = getattr(django_settings, 'META_TWITTER_TYPES', TWITTER_TYPES)
TWITTER_SITE = getattr(django_settings, 'META_TWITTER_SITE', False)
TWITTER_AUTHOR = getattr(django_settings, 'META_TWITTER_AUTHOR', False)
GPLUS_TYPE = getattr(django_settings, 'META_GPLUS_TYPE', False)
GPLUS_TYPES = getattr(django_settings, 'META_GPLUS_TYPES', GPLUS_TYPES)
GPLUS_AUTHOR = getattr(django_settings, 'META_GPLUS_AUTHOR', False)

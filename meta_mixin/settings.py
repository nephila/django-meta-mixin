# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings as django_settings

DEFAULT_IMAGE = getattr(django_settings, 'META_DEFAULT_IMAGE', False)
DEFAULT_TYPE = getattr(django_settings, 'META_SITE_TYPE', False)
FB_TYPE = getattr(django_settings, 'META_FB_TYPE', False)
FB_APPID = getattr(django_settings, 'META_FB_APPID', False)
FB_PROFILE_ID = getattr(django_settings, 'META_FB_PROFILE_ID', False)
FB_PUBLISHER = getattr(django_settings, 'META_FB_PUBLISHER', False)
FB_AUTHOR_URL = getattr(django_settings, 'META_FB_AUTHOR_URL', False)
TWITTER_TYPE = getattr(django_settings, 'META_TWITTER_TYPE', False)
TWITTER_SITE = getattr(django_settings, 'META_TWITTER_SITE', False)
TWITTER_AUTHOR = getattr(django_settings, 'META_TWITTER_AUTHOR', False)
GPLUS_TYPE = getattr(django_settings, 'META_GPLUS_TYPE', False)
GPLUS_AUTHOR = getattr(django_settings, 'META_GPLUS_AUTHOR', False)

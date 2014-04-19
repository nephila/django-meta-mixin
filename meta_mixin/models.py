# -*- coding: utf-8 -*-
from copy import copy
from . import settings


class ModelMeta(object):
    """
    Meta information mixin.
    """
    _metadata = {}
    _metadata_default = {
        'title': False,
        'description': False,
        'og_description': False,
        'twitter_description': False,
        'gplus_description': False,
        'keywords': False,
        'locale': None,
        'image': settings.DEFAULT_IMAGE,
        'object_type': settings.DEFAULT_TYPE,
        'og_type': settings.FB_TYPE,
        'og_app_id': settings.FB_APPID,
        'og_profile_id': settings.FB_PROFILE_ID,
        'og_publisher': settings.FB_PUBLISHER,
        'og_author_url': settings.FB_AUTHOR_URL,
        'twitter_type': settings.TWITTER_TYPE,
        'twitter_site': settings.TWITTER_SITE,
        'twitter_author': settings.TWITTER_AUTHOR,
        'gplus_type': settings.GPLUS_TYPE,
        'gplus_author': settings.GPLUS_AUTHOR,
        'published_time': False,
        'modified_time': False,
        'expiration_time': False,
        'tag': False,
        'url': False,
    }

    def as_meta(self):
        """
        Method that generates the Meta object (from django-meta)
        """
        from meta.views import Meta
        metadata = copy(self._metadata)
        metadata.update(self._metadata_default)
        meta = Meta()
        for field, value in self._metadata.items():
            if value:
                attr = getattr(self, value, False)
                if attr is not False:
                    if callable(attr):
                        data = attr()
                    else:
                        data = attr
                else:
                    data = value
                setattr(meta, field, data)
        for field in ('og_description', 'twitter_description',
                      'gplus_description'):
            generaldesc = getattr(meta, 'description', False)
            if not getattr(meta, field, False) and generaldesc:
                setattr(meta, field, generaldesc)
        return meta

    def get_author(self):
        """
        Retrieve the author object. This is meant to be overridden in the model
        to return the actual author instance (e.g.: the user object).
        """
        class Author(object):
            fb_url = None
            twitter_profile = None
            gplus_profile = None

            def get_full_name(self):  # pragma: no cover
                return None
        return Author()

    def get_author_url(self):
        try:
            return self.get_author().fb_url
        except AttributeError:  # pragma: no cover
            return ''

    def get_author_name(self):
        try:
            return self.get_author().get_full_name()
        except AttributeError:  # pragma: no cover
            return ''

    def get_author_twitter(self):
        try:
            return self.get_author().twitter_profile
        except AttributeError:  # pragma: no cover
            return ''

    def get_author_gplus(self):
        try:
            return self.get_author().gplus_profile
        except AttributeError:  # pragma: no cover
            return ''
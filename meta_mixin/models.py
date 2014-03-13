# -*- coding: utf-8 -*-
class ModelMeta(object):
    """
    Meta information mixin.
    """
    _metadata = {
        'title': False,
        'description': False,
        'og_description': False,
        'twitter_description': False,
        'gplus_description': False,
        'keywords': False,
        'locale': None,
        'image': False,
        'object_type': False,
        'og_type': False,
        'og_app_id': False,
        'og_profile_id': False,
        'og_publisher': False,
        'og_author_url': False,
        'twitter_type': False,
        'twitter_site': False,
        'twitter_author': False,
        'gplus_type': False,
        'gplus_author': False,
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
        meta = None
        try:
            from meta.views import Meta
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
        except ImportError:
            pass
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

            def get_full_name(self):
                return None
        return Author()

    def get_author_url(self):
        try:
            return self.get_author().fb_url
        except AttributeError:
            return ''

    def get_author_name(self):
        try:
            return self.get_author().get_full_name()
        except AttributeError:
            return ''

    def get_author_twitter(self):
        try:
            return self.get_author().twitter_profile
        except AttributeError:
            return ''

    def get_author_gplus(self):
        try:
            return self.get_author().gplus_profile
        except AttributeError:
            return ''
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from datetime import timedelta

from django.test.utils import override_settings
from django.utils import timezone
from djangocms_helper.base_test import BaseTestCase
from example_app.models import Post
from meta_mixin.models import ModelMeta
from meta_mixin.templatetags.meta_extra import generic_prop, googleplus_scope


class TestMeta(BaseTestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='a title',
            slug='title',
            abstract='post abstract',
            meta_description='post meta',
            meta_keywords='post keyword1,post keyword 2',
            author=self.user,
            date_published_end=timezone.now() + timedelta(days=2),
            text='post text',
            main_image='/path/to/image'
        )

    @override_settings(META_SITE_PROTOCOL='http')
    def test_as_meta(self):
        expected = {
            'locale': 'dummy_locale',
            'image': 'http://example.com/path/to/image',
            'object_type': 'Article',
            'tag': False,
            'keywords': ['post keyword1', 'post keyword 2'],
            'og_profile_id': '1111111111111',
            'twitter_description': 'post meta',
            'gplus_type': 'Article',
            'title': 'a title',
            'gplus_description': 'post meta',
            'expiration_time': self.post.date_published_end,
            'og_description': 'post meta',
            'description': 'post meta',
            'twitter_type': 'Summary',
            'modified_time': self.post.date_modified,
            'og_author_url': 'https://facebook.com/foo.bar',
            'og_app_id': False,
            'gplus_author': '+FooBar',
            'published_time': self.post.date_published,
            'url': 'http://example.com/title/',
            'og_publisher': 'https://facebook.com/foo.blag',
            'og_type': 'Article',
            'twitter_author': '@FooBar',
            'twitter_site': '@FooBlag',
        }
        meta = self.post.as_meta()
        self.assertTrue(meta)
        for key in ModelMeta._metadata_default.keys():
            value = expected[key]
            if value is not False:
                self.assertEqual(value, getattr(meta, key))
            else:
                self.assertFalse(hasattr(meta, key))

        self.assertEqual(self.post.build_absolute_uri('hi'), 'http://example.com/hi')
        self.assertEqual(self.post.build_absolute_uri('http://example.com/hi'), 'http://example.com/hi')

    def test_as_meta_with_request(self):
        # Server is different as it's taken directly from the request object
        expected = {
            'locale': 'dummy_locale',
            'image': 'https://testserver/path/to/image',
            'object_type': 'Article',
            'tag': False,
            'keywords': ['post keyword1', 'post keyword 2'],
            'og_profile_id': '1111111111111',
            'twitter_description': 'post meta',
            'gplus_type': 'Article',
            'title': 'a title',
            'gplus_description': 'post meta',
            'expiration_time': self.post.date_published_end,
            'og_description': 'post meta',
            'description': 'post meta',
            'twitter_type': 'Summary',
            'modified_time': self.post.date_modified,
            'og_author_url': 'https://facebook.com/foo.bar',
            'og_app_id': False,
            'gplus_author': '+FooBar',
            'published_time': self.post.date_published,
            'url': 'https://testserver/title/',
            'og_publisher': 'https://facebook.com/foo.blag',
            'og_type': 'Article',
            'twitter_author': '@FooBar',
            'twitter_site': '@FooBlag',
        }
        request = self.get_request(None, 'en', path='/title/', secure=True)
        meta = self.post.as_meta(request)
        self.assertTrue(meta)
        for key in ModelMeta._metadata_default.keys():
            value = expected[key]
            if value is not False:
                self.assertEqual(value, getattr(meta, key))
            else:
                self.assertFalse(hasattr(meta, key))

    def test_templatetag(self):
        meta = self.post.as_meta()
        response = self.client.get('/title/')
        self.assertContains(response, 'itemscope itemtype="http://schema.org/Article"')
        self.assertContains(response, 'article:published_time"')
        self.assertContains(response, '<meta name="twitter:image:src" content="http://example.com/path/to/image">')
        self.assertContains(response, '<link rel="author" href="https://plus.google.com/%s"/>' % meta.gplus_author)
        self.assertContains(response, '<meta itemprop="description" content="%s">' % self.post.meta_description)
        self.assertContains(response, '<meta name="twitter:description" content="%s">' % self.post.meta_description)
        self.assertContains(response, '<meta property="og:description" content="%s">' % self.post.meta_description)
        self.assertContains(response, '<meta name="description" content="%s">' % self.post.meta_description)
        self.assertContains(response, '<meta name="keywords" content="%s">' % ", ".join(self.post.meta_keywords.split(",")))

    @override_settings(META_USE_OG_PROPERTIES=False)
    def test_templatetag_no_og(self):
        from meta import settings
        settings.USE_OG_PROPERTIES = False
        response = self.client.get('/title/')
        self.assertFalse(response.rendered_content.find('og:description') > -1)
        self.assertContains(response, '<meta itemprop="description" content="%s">' % self.post.meta_description)
        self.assertContains(response, '<meta name="twitter:description" content="%s">' % self.post.meta_description)
        self.assertContains(response, '<meta name="keywords" content="%s">' % ", ".join(self.post.meta_keywords.split(",")))

    def test_generic_prop_basically_works(self):
        """
        Test vendorized generic_prop templatetag
        """
        self.assertEqual(
            generic_prop('og', 'type', 'website'),
            '<meta property="og:type" content="website">'
        )

    def test_google_plus_scope_works(self):
        """
        Test vendorized googleplus_scope templatetag
        """
        self.assertEqual(
            googleplus_scope('bar'),
            ' itemscope itemtype="http://schema.org/bar" '
        )

    @override_settings(META_SITE_PROTOCOL='https')
    def test_image_protocol(self):
        from meta import settings
        settings.SITE_PROTOCOL = 'https'
        meta = self.post.as_meta()
        self.assertEqual('https://example.com/path/to/image', getattr(meta, 'image'))

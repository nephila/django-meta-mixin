=================
django-meta-mixin
=================

.. image:: https://img.shields.io/pypi/v/django-meta-mixin.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-meta-mixin
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/django-meta-mixin.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-meta-mixin
    :alt: Monthly downloads

.. image:: https://img.shields.io/pypi/pyversions/django-meta-mixin.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-meta-mixin
    :alt: Python versions

.. image:: https://img.shields.io/travis/nephila/django-meta-mixin.svg?style=flat-square
    :target: https://travis-ci.org/nephila/django-meta-mixin
    :alt: Latest Travis CI build status

.. image:: https://img.shields.io/coveralls/nephila/django-meta-mixin/master.svg?style=flat-square
    :target: https://coveralls.io/r/nephila/django-meta-mixin?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/codecov/c/github/nephila/django-meta-mixin/master.svg?style=flat-square
    :target: https://codecov.io/github/nephila/django-meta-mixin
    :alt: Test coverage

.. image:: https://codeclimate.com/github/nephila/django-meta-mixin/badges/gpa.svg?style=flat-square
   :target: https://codeclimate.com/github/nephila/django-meta-mixin
   :alt: Code Climate


Concepts
--------

**django-meta-mixin** provides a mixin to handle metadata in your models.

Actual data are evaluated at runtime pulling values from model attributes and
methods.

To use it, defines a ``_metadata`` attribute as a dictionary of tag/value pairs;

* **tag** is the name of the metatag as used by ``meta.html`` template
* **value** is a string that is evaluated in the following order:

  * model method name called with the meta attribute as argument
  * model method name called with no arguments
  * model attribute name (evaluated at runtime)
  * string literal (if none of the above exists)

If **value** is ``False`` or it is evaluated as ``False`` at runtime the tag is skipped.

To use this mixin you must invoke ``as_meta()`` on the model instance
for example in the get_context_data().

Request
+++++++

``as_meta()`` accepts the ``request`` object that is saved locally and is available to methods by
using the ``get_request`` method.


Public interface
++++++++++++++++

``ModelMeta.get_meta(request=None)``: returns the metadata attributes definition. Tipically these
are set in ``_metadata`` attribute in the model;

``ModelMeta.as_meta(request=None)``: returns the meta representation of the object suitable for
use in the template;

``ModelMeta.get_request()``: returns the ``request`` object, if given as argument to ``as_meta``;

``ModelMeta.get_author()``: returns the author object for the current instance. Default
implementation does not return a valid object, this **must** be overidden in the application
according to what is an author in the application domain;

``ModelMeta.build_absolute_uri(url)``: create an absolute URL (i.e.: complete with protocol and
domain); this is generated from the ``request`` object, if given as argument to ``as_meta``;


Installation
------------

From PyPi::

    pip install django-meta-mixin

From github::

    pip install -e git+https://github.com/nephila/django-meta-mixin#egg=django-meta-mixin

Usage
-----

#. Add to installed apps along with ``django-meta``::

    INSTALLED_APPS = [
        ...
        'meta',
        'meta_mixin',
    ]

#. Configure ``django-meta`` according to documentation
   (https://github.com/nephila/django-meta#configuration)

#. Add meta information to your model::

    from django.db import models
    from meta_mixin.models import ModelMeta

    class MyModel(ModelMeta, models.Model):
        name = models.CharField(max_length=20)
        abstract = models.TextField()
        ...

        _metadata = {
            'title': 'name',
            'description': 'abstract',
            ...
        }

#. Push metadata in the context using ``as_meta`` method::

    class MyView(DetailView):

        ...

        def get_context_data(self, **kwargs):
            context = super(MyView, self).get_context_data(self, **kwargs)
            context['meta'] = self.get_object().as_meta(self.request)
            return context

#. Include ``meta_mixin/meta.html`` template in your templates::

    {% load sekizai_tags %}

    <html {% render_block 'html_extra' %}>
    <head>
        {% include "meta_mixin/meta.html" %}
    </head>
    <body>
    </body>
    </html>

Note
++++
For Google+ support you must add ``{% render_block 'html_extra' %}`` in your template to add object type definition. See relevant Google+ snippets documentation (https://developers.google.com/+/web/snippet/)

Example
+++++++

Look at the ``example`` folder for a sample implementation.

Available properties
--------------------

**django-meta-mixin** currently supports the following properties:

Generic properties
++++++++++++++++++
* title: object title,
* description: generic object description, used for SEO and as default for specific description,
* keywords: generic keywords for SEO
* locale: advertised object locale (if any)
* image: image to display for object
* object_type: default object type
* published_time: date-time of publishing
* modified_time: date-time of modification
* expiration_time: date-time of expiration
* url: canonical object url

Open Graph properties
+++++++++++++++++++++
* og_description: object description in Open Graph
* og_type: object type in Open Graph
* og_app_id: Facebook App ID
* og_profile_id: Author's Facebook profileID
* og_publisher: Facebook URL to publisher's profile
* og_author_url: Facebook URL to author's profile
* tag: object tags


Twitter Cards properties
++++++++++++++++++++++++
* twitter_description: object description on Twitter card (currently 200 chars max)
* twitter_type: twitter card type
* twitter_site: Website twitter account
* twitter_author: Author twitter account


Google+ Snippet properties
++++++++++++++++++++++++++
* gplus_description: object description
* gplus_type: object type according to schema.org types
* gplus_author: Author Google+ account

Settings
--------

Some of the above properties can be set either in the model or via settings paramaters

* image: ``META_DEFAULT_IMAGE`` (must be an absolute URL)
* object_type: ``META_SITE_TYPE``
* og_type: ``META_FB_TYPE``
* og_app_id: ``META_FB_APPID``
* og_profile_id: ``META_FB_PROFILE_ID``
* og_publisher: ``META_FB_PUBLISHER``
* og_author_url: ``META_FB_AUTHOR_URL``
* twitter_type: ``META_TWITTER_TYPE``
* twitter_site: ``META_TWITTER_SITE``
* twitter_author: ``META_TWITTER_AUTHOR``
* gplus_type: ``META_GPLUS_TYPE``
* gplus_author: ``META_GPLUS_AUTHOR``

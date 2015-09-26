# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from meta.templatetags.meta import *  # NOQA  # nopyflakes


@register.simple_tag
def generic_prop(namespace, name, value):
    """
    Generic property setter that allows to create custom namespaced meta:
    e.g.: fb:profile_id.
    """
    return '<meta property="%s:%s" content="%s">' % (namespace, name, value)


@register.simple_tag
def googleplus_scope(value):
    """
    This is meant to be used as attribute to html / body or other tags to
    define schema.org type.
    """
    return ' itemscope itemtype="http://schema.org/%s" ' % value

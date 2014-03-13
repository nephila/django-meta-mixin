# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import template

register = template.Library()


@register.simple_tag
def og_prop(name, value):
    """
    Support for generic OpenGraph property
    """
    return generic_prop('og', name, value)


@register.simple_tag
def twitter_prop(name, value):
    """
    Support for generic twitter property
    """
    return '<meta name="twitter:%s" content="%s">' % (name, value)


@register.simple_tag
def googleplus_prop(name, value):
    """
    Support for generic schema.org property
    """
    return '<meta itemprop="%s" content="%s">' % (name, value)


@register.simple_tag
def meta(name, value):
    """
    Support for generic meta tag
    """
    return '<meta name="%s" content="%s">' % (name, value)


@register.simple_tag
def meta_list(name, lst):
    """
    Render a list of items in the generic meta tag
    """
    try:
        return meta(name, ', '.join(lst))
    except:
        return ''


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

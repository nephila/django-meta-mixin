# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from .views import PostDetailView

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>\w[-\w]*)/$', PostDetailView.as_view(), name='post-detail'),
)

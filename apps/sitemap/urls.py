# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from django.contrib.sitemaps.views import sitemap, index

from .entries import StaticViewSitemap

sitemaps = {
       'statics' : StaticViewSitemap
}

urlpatterns = patterns('',
    url(r'^sitemap\.xml$', index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', sitemap, {'sitemaps': sitemaps}),
)


# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse



class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home',
                'legal-mentions',
                'shop-contact']

    def location(self, item):
        return reverse(item)

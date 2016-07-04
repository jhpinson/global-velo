# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    (r'^nos-partnaires\.html$', views.Partners.as_view(), {}, "shop-partners"),
    url(r'^(?P<pk>\d+)/(?P<slug>\S+)$', views.PartnerDetail.as_view(), {}, "partner_detail_view"),
)
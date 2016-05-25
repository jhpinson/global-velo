# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    (r'^location-de-velos/$', views.BikeRental.as_view(), {}, "bike-rental"),
    (r'^nos-velos/$', views.BikeSell.as_view(), {}, "bike-sell"),
    
)
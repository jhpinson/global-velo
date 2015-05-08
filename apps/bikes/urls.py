# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = patterns('',
    (r'^location-de-velos\.html$', views.BikeRental.as_view(), {}, "bike-rental"),
    (r'^conseils-pour-choisir-son-velo\.html$', TemplateView.as_view(template_name="bike/choose-your-bike.html"), {}, "bike-choose-your-bike"),
)
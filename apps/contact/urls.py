# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = patterns('',
  url(r'^nous-contacter\.html$', views.Contact.as_view(), name='shop-contact'),
  url(r'^message-envoye.html$', views.ContactSent.as_view(), name='contact-sent'),
)
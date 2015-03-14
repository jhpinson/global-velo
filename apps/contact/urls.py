# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from . import views

urlpatterns = patterns('',
  url(r'^contact.html$', views.Contact.as_view(), name='contact-send'),
  url(r'^message-envoye.html$', TemplateView.as_view(template_name='contact/sent.html'), name='contact-sent'),
)
# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
  url(r'^creer-un-compte.html$', views.CreateUser.as_view(), name = 'users-user-create'),
  url(r'^se-deconnecter.html$', views.Logout.as_view(), name = 'users-user-logout'),
  url(r'^se-connecter.html$', views.Login.as_view(), name = 'users-user-login'),
)
# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from . import models
from django.conf import settings


class Partner(OrderedModelAdmin, admin.ModelAdmin):

    list_display = 'name', 'move_up_down_links'

    class Media:
        js = (
              settings.STATIC_URL+'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              settings.STATIC_URL+'js/admin/tinymce_setup.js',
              )

admin.site.register(models.Partner, Partner)
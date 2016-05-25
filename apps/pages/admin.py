# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from . import models
from django.conf import settings

class Page(AdminImageMixin, admin.ModelAdmin):

    class Media:
        js = (
              settings.STATIC_URL+'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              settings.STATIC_URL+'js/admin/tinymce_setup.js',
              )

    list_display = 'title', 'subtitle', 'visible'
    list_editable = 'visible',
    

admin.site.register(models.Page, Page)

class Section(AdminImageMixin, admin.ModelAdmin):
    list_display = 'title',
    

admin.site.register(models.Section, Section)
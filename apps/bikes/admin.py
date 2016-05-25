# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from . import models
from django.conf import settings


class Size(admin.ModelAdmin):
    list_display = 'label',


class Category(admin.ModelAdmin):
    list_display = 'label',


class Brand(admin.ModelAdmin):
    list_display = 'title',


class Bike(AdminImageMixin, admin.ModelAdmin):
    list_display = ('label', 'for_sale')

    class Media:
        js = (
              settings.STATIC_URL+'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
              settings.STATIC_URL+'js/admin/tinymce_setup.js',
              )

    raw_id_fields = ('sizes', 'categories', 'brand')
    autocomplete_lookup_fields = {
        'm2m': ['sizes', 'categories', 'brand'],
    }


admin.site.register(models.Bike, Bike)
admin.site.register(models.Size, Size)
admin.site.register(models.Category, Category)
admin.site.register(models.Brand, Brand)
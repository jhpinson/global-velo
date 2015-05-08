# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from . import models


class Size(admin.ModelAdmin):
    list_display = 'label',


class Category(admin.ModelAdmin):
    list_display = 'label',


class Bike(AdminImageMixin, admin.ModelAdmin):
    list_display = 'label',

    raw_id_fields = ('sizes', 'categories')
    autocomplete_lookup_fields = {
        'm2m': ['sizes', 'categories'],
    }


admin.site.register(models.Bike, Bike)
admin.site.register(models.Size, Size)
admin.site.register(models.Category, Category)
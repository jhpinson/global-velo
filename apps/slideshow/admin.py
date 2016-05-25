# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from . import models

class Slide(AdminImageMixin, admin.ModelAdmin):
    list_display = 'title', 'subtitle', 'visible'
    list_editable = 'visible',
    

admin.site.register(models.Slide, Slide)


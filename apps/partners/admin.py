# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from . import models

class Partner(OrderedModelAdmin, admin.ModelAdmin):

    list_display = 'name', 'move_up_down_links'

admin.site.register(models.Partner, Partner)
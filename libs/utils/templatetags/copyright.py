# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def copyright_year():
    return datetime.now().year

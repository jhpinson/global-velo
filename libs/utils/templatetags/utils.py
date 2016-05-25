# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def copyright_year():
    return datetime.now().year


        
@register.filter
def verbose(value, arg):
    """
    Usage:
        {{ name|verbose:"Hello %s this is a dummy text" }}
        {{ image|verbose:"<img src=\"%s\" />" }}
    """
    try:    
        if not value:
            return ''
        return arg % value
    except Exception:
        return str(value)

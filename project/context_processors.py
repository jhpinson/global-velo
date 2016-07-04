# -*- coding: utf-8 -*-
from django.conf import settings

def common(context):
    return {
        'DOMAIN': settings.DOMAIN, 
        'SITE_TAGLINE':'Global Vélo – location, vente et réparation de vélos à Nay',        
    }

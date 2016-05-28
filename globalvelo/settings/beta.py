# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import os

from .deps import *

ALLOWED_HOSTS = ['www.global-velo.pro', 'beta.global-velo.pro']

MEDIA_URL = 'http://beta-medias.global-velo.pro/'
STATIC_URL = 'http://beta-statics.global-velo.pro/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('MAILJET_USER', '127.0.0.1')
EMAIL_HOST_PASSWORD = os.environ.get('MAILJET_PASSWORD', '127.0.0.1')
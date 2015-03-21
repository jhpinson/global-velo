from cache import *
from common import *
from pipeline import *
from os import environ

DEBUG = False
PIPELINE_AUTO = True
PIPELINE_VERSION = False
PIPELINE_VERSIONING = 'pipeline.versioning.mtime.MTimeVersioning'

PIPELINE_STYLUS_BINARY = "/usr/local/bin/stylus"


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)


ALLOWED_HOSTS = 'www.global-velo.pro', 'beta.global-velo.pro',

MEDIA_URL = 'http://medias.global-velo.pro/'
STATIC_URL = 'http://statics.global-velo.pro/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = environ.get('MAILJET_USER', '127.0.0.1')
EMAIL_HOST_PASSWORD = environ.get('MAILJET_PASSWORD', '127.0.0.1')
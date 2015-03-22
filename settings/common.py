# Django settings for project.

import sys
from path import path
from os import environ

PROJECT_ROOT = path(__file__).abspath().dirname().dirname()
SITE_ROOT = PROJECT_ROOT.dirname()
PROJECT_NAME = SITE_ROOT.basename()

sys.path.append(SITE_ROOT)
sys.path.append(PROJECT_ROOT / 'apps')
sys.path.append(PROJECT_ROOT / 'libs') 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_HOST = 'localhost'

ADMINS = (
    ('Jean-Hugues Pinson', 'jean-hugues@jacquieetmichel.net'),
)
CONTACT_EMAIL = environ.get('CONTACT_EMAIL', 'jean-hugues@jacquieetmichel.net')
DEFAULT_FROM_EMAIL = 'no-reply@global-velo.pro'
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME' :  environ.get('APP_DATABASE_NAME', PROJECT_NAME),
        'USER' : environ.get('APP_DATABASE_USER', None),
        'PASSWORD' : environ.get('APP_DATABASE_PASSWORD', None),
        'HOST' : environ.get('APP_DATABASE_HOST', 'localhost'),
        'PORT' : environ.get('APP_DATABASE_PORT', ''),

    }
}

TIME_ZONE = 'Europe/Paris'

LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = SITE_ROOT / 'data/medias/'

MEDIA_URL = '/medias/'

STATIC_ROOT = SITE_ROOT / 'data/statics/'

STATIC_URL = '/statics/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '87#ngnl9*lnvkh73kvvh5j76)d7f8i^edws2@&*!$bmb(6sv9='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT / 'templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.sitemaps',

    PROJECT_NAME,
    'pipeline',
    'crispy_forms',
    'password_reset',
    'utils',

    #models
    'users',
    'contact',
)

TEMPLATE_CONTEXT_PROCESSORS =  ('django.contrib.auth.context_processors.auth',
 'django.core.context_processors.request',
 'django.core.context_processors.debug',
 'django.core.context_processors.i18n',
 'django.core.context_processors.media',
 'django.core.context_processors.static',
 'django.core.context_processors.tz',
 'django.contrib.messages.context_processors.messages')

CRISPY_TEMPLATE_PACK = 'bootstrap3'
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
AUTH_USER_MODEL= 'users.User'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

GRAPPELLI_CLEAN_INPUT_TYPES = False
TEST_RUNNER = "django.test.simple.DjangoTestSuiteRunner"

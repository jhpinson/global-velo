# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from .deps import *

CACHES['mint']['BACKEND'] = 'django.core.cache.backends.dummy.DummyCache'
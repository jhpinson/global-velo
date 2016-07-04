# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import os

THUMBNAIL_QUALITY = 80
THUMBNAIL_DEBUG = False
THUMBNAIL_PRESERVE_FORMAT = True
THUMBNAIL_PROGRESSIVE = True

THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_REDIS_PORT = os.environ.get('REDIS_THUMBNAIL_CACHE_PORT', '6379')
THUMBNAIL_REDIS_HOST = os.environ.get('REDIS_THUMBNAIL_CACHE_HOST', '127.0.0.1')
THUMBNAIL_REDIS_DB = os.environ.get('REDIS_THUMBNAIL_CACHE_DB', '4')
# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import os


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_DEFAULT_CACHE_HOST', '127.0.0.1') + ':' + os.environ.get('REDIS_DEFAULT_CACHE_PORT', '6379') + ':' + os.environ.get('REDIS_DEFAULT_CACHE_DB', '1'),
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    },

    'mint': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_MINT_CACHE_HOST', '127.0.0.1') + ':' + os.environ.get('REDIS_MINT_CACHE_PORT', '6379') + ':' + os.environ.get('REDIS_MINT_CACHE_DB', '2'),
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CLIENT_CLASS' : 'mcache.client.mint.MintClient'
        }
    },

    'sessions': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('REDIS_SESSION_CACHE_HOST', '127.0.0.1') + ':' + os.environ.get('REDIS_SESSION_CACHE_PORT', '6379') + ':' + os.environ.get('REDIS_SESSION_CACHE_DB', '3'),
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    },
}


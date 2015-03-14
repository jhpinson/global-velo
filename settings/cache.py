from os import environ
import common
from os import environ



# cacheops
"""
common.INSTALLED_APPS += (
    'cacheops',
)

common.CACHEOPS = {
    '*.*': ('all', 60*10)
}

common.CACHEOPS_REDIS = {
    'host':  environ.get('REDIS_HOST', '127.0.0.1') ,
    'port': 6379,
    'db': 1,
    'socket_timeout': 4,
}
"""

# default cache
common.CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': environ.get('REDIS_HOST', '127.0.0.1') + ':6379',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser'
        }
    }
}

# Thumbnail
common.THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
common.THUMBNAIL_REDIS_DB = 2


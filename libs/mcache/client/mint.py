# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import time
import warnings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from redis.exceptions import ConnectionError
from redis_cache.client import DefaultClient
from redis_cache.exceptions import ConnectionInterrupted

MINT_DELAY = 120


class MintClient(DefaultClient):

    def get_many(self, keys, version=None, client=None):
        warnings.warn("get_many is not use in this client.")

    def set_many(self, data, timeout=DEFAULT_TIMEOUT, version=None, client=None):
        warnings.warn("set_many is not use in this client.")

    def _incr(self, key, delta=1, version=None, client=None):
        warnings.warn("_incr is not use in this client.")

    def incr_version(self, key, delta=1, version=None, client=None):
        warnings.warn("incr_version is not use in this client.")

    def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None, client=None, nx=False):
        """
        Persist a value to the cache, and set an optional expiration time.
        Also supports optional nx parameter. If set to True - will use redis setnx instead of set.
        """

        if not client:
            client = self.get_client(write=True)

        key = self.make_key(key, version=version)
        value = self.pickle(value)

        if timeout is True:
            warnings.warn("Using True as timeout value, is now deprecated.", DeprecationWarning)
            timeout = self._backend.default_timeout

        if timeout == DEFAULT_TIMEOUT:
            timeout = self._backend.default_timeout

        try:
            if nx:
                warnings.warn("UNX not implemented.")
                """res = client.setnx(key, value)
                if res and timeout is not None and timeout > 0:
                    return client.expire(key, int(timeout))
                return res"""
            else:
                if timeout is None:
                    raise Exception('timeout is none')

                if timeout > 0:

                    with client.pipeline() as pipeline:
                        pipeline.delete(key)
                        pipeline.rpush(key, int(time.time()) + int(timeout), value)
                        pipeline.expire(key, int(timeout) + MINT_DELAY)
                        pipeline.execute()

                        return

        except ConnectionError:
            raise ConnectionInterrupted(connection=client)

    def get(self, key, default=None, version=None, client=None):
        """
        Retrieve a value from the cache.

        Returns unpickled value if key is found, the default if not.
        """
        if client is None:
            client = self.get_client(write=False)

        key = self.make_key(key, version=version)

        try:
            t = client.lindex(key, 0)
            if t is None or int(t) < int(time.time()):
                if t is not None:
                    # try to acquire lock to refresh cache
                    lock = "%s-lock" % key
                    with client.pipeline() as pipeline:
                        pipeline.setnx(lock, 1)
                        pipeline.expire(lock, 5)
                        res = pipeline.execute()

                    # lock not acquired
                    if res[0] is False:
                        return client.lindex(key, 1)

                    # lock acquired
                    with client.pipeline() as pipeline:
                        pipeline.lset(key, 0, int(t) + MINT_DELAY)
                        pipeline.delete(lock)
                        pipeline.execute()

                return default
            else:
                value = client.lindex(key, 1)
        except ConnectionError:
            raise ConnectionInterrupted(connection=client)

        if value is None:
            return default

        return self.unpickle(value)
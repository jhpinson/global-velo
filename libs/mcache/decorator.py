# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from functools import wraps
from django.utils.decorators import available_attrs, decorator_from_middleware_with_args
from mcache.middlewares import CacheMiddleware


def cache_page(*args, **kwargs):
    """
    Copy/paste from django code
    """
    # We also add some asserts to give better error messages in case people are
    # using other ways to call cache_page that no longer work.
    if len(args) != 1 or callable(args[0]):
        raise TypeError("cache_page has a single mandatory positional argument: timeout")
    cache_timeout = args[0]
    cache_alias = kwargs.pop('cache', None)
    key_prefix = kwargs.pop('key_prefix', None)
    if kwargs:
        raise TypeError("cache_page has two optional keyword arguments: cache and key_prefix")

    return decorator_from_middleware_with_args(CacheMiddleware)(
        cache_timeout=cache_timeout, cache_alias=cache_alias, key_prefix=key_prefix
    )


def cache_for_non_staff(timeout, cache='default'):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                return cache_page(timeout, cache=cache)(view_func)(request, *args, **kwargs)
        return _wrapped_view
    return decorator
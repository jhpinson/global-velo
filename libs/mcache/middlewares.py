# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import cgi
import functools
from urllib import urlencode

from urlparse import urlsplit, urljoin
from django.middleware.cache import CacheMiddleware as DjangoCacheMiddleware
from django.utils.encoding import iri_to_uri

class RequestPathChanged(object):

    def __init__(self, request, keys=None):
        self.request = request
        self._keys = keys
        self._prev_get_full_path = request.get_full_path

    def __enter__(self):
        self.request.get_full_path = functools.partial(
                self.get_full_path,
                self.request,
                self._keys
            )

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.request.get_full_path = self._prev_get_full_path

    def get_full_path(self, request, keys):
        qs = request.META.get('QUERY_STRING', '')

        if self._keys is not None and len(self._keys) > 0:
            parsed = cgi.parse_qs(qs)
            keep = dict((k, parsed[k]) for k in parsed if k in keys)
            qs = urlencode(keep, True)
        else:
            qs = ''

        return '%s%s' % (request.path, ('?' + iri_to_uri(qs)) if qs else '')


class CacheMiddleware(DjangoCacheMiddleware):

    def process_request(self, request):
        with RequestPathChanged(request):
            return super(CacheMiddleware, self).process_request(request)


    def process_response(self, request, response):

        with RequestPathChanged(request):
            return super(CacheMiddleware, self).process_response(request, response)


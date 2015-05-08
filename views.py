from __future__ import absolute_import, unicode_literals
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView

class RobotsTxt(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
    @method_decorator(cache_page(86400, cache='mint'))
    def dispatch(self, request, *args, **kwargs):
        return super(RobotsTxt, self).dispatch(request, *args, **kwargs)

class Home(TemplateView):

    template_name = 'home.html'

    @method_decorator(cache_page(60, cache='mint'))
    def dispatch(self, request, *args, **kwargs):
        return super(Home, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Home, self).get_context_data(*args, **kwargs)
        return context

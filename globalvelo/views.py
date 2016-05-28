from __future__ import absolute_import, unicode_literals
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView


from pages.models import Page, Section
from partners.models import Partner
from slideshow.models import Slide

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
        context['slides'] = Slide.objects.filter(visible=True)
        
        return context


class Magasin(TemplateView):

    template_name = 'magasin.html'


    @method_decorator(cache_page(60, cache='mint'))
    def dispatch(self, request, *args, **kwargs):
        return super(Magasin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Magasin, self).get_context_data(*args, **kwargs)
        section = Section.objects.get(pk=1)
        context['pages'] = Page.objects.filter(section=section, visible=True).order_by('id')
        context['partners'] = Partner.objects.filter(active=True)
        
        return context

class Mentions(TemplateView):

    template_name = 'default.html'


    @method_decorator(cache_page(60, cache='mint'))
    def dispatch(self, request, *args, **kwargs):
        return super(Mentions, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Mentions, self).get_context_data(*args, **kwargs)
        section = Section.objects.get(pk=4)
        context['pages'] = Page.objects.filter(section=section, visible=True).order_by('order')
        
        return context

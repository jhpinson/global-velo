# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import models

class Partners(ListView):

    template_name='shop/partners.html'

    context_object_name = 'partners'

    def get_queryset(self):

        return models.Partner.objects.filter(active=True)


class PartnerDetail(DetailView):
    model = models.Partner
    template_name = "partner.html"
    
    def get_context_data(self, **kwargs):
        
        context = super(PartnerDetail, self).get_context_data(**kwargs)
        
        context['partners'] = models.Partner.objects.all()
        return context
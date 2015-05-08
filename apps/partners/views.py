# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from django.views.generic.list import ListView

from . import models

class Partners(ListView):

    template_name='shop/partners.html'

    context_object_name = 'partners'

    def get_queryset(self):

        return models.Partner.objects.filter(active=True)
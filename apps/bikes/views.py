# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from django.views.generic.base import TemplateView

from . import models

class BikeRental(TemplateView):

    template_name = 'bike/bike-rental-pending.html'

    def get_context_data(self, **kwargs):

        context = super(BikeRental, self).get_context_data(**kwargs)

        context['categories'] = models.Category.objects.all()
        context['bikes'] = models.Bike.objects.all()


        return context


# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import json

from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from pages.models import Page, Section
from bikes.models import Bike, Category

from contact.forms import Contact as ContactForm, RentalContact
from contact.views import Contact as ContactView



from django import forms
from crispy_forms.helper import FormHelper

from utils.ajax import serialize_form_errors


class BikeRental(FormView):

    template_name = 'locations.html'
    form_class = RentalContact

    def form_invalid(self, form):
        return HttpResponse(json.dumps({
            "success": False,
            "errors": serialize_form_errors(form)
        }), content_type='application/json')

    def form_valid(self, form):
        form.send_message()
        response = {'success' : True, 'reset' : True}
        return HttpResponse(json.dumps(response), content_type='application/json')


    def get_context_data(self, **kwargs):

        context = super(BikeRental, self).get_context_data(**kwargs)

        section = Section.objects.get(pk=2)
        context['pages'] = Page.objects.filter(section=section, visible=True)

        context['categories'] = Category.objects.all()
        context['bikes'] = Bike.objects.filter(for_sale=False, visible=True)
        return context



class BikeSell(TemplateView):

    template_name = 'vente.html'


    def get_context_data(self, **kwargs):

        context = super(BikeSell, self).get_context_data(**kwargs)

        section = Section.objects.get(pk=3)
        context['pages'] = Page.objects.filter(section=section, visible=True)

        context['categories'] = Category.objects.all()
        context['form'] = ContactForm
        context['bikes'] = Bike.objects.filter(for_sale=True, visible=True)

        return context        

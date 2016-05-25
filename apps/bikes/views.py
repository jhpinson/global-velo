# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from pages.models import Page, Section
from bikes.models import Bike, Category

from contact.forms import Contact as ContactForm
from contact.views import Contact as ContactView


from phonenumber_field.modelfields import PhoneNumberField

from django import forms
from crispy_forms.helper import FormHelper

class BikeRentalForm(forms.Form):
    
    email = forms.EmailField(label='Adresse e-mail')
    phone = forms.CharField(label="Téléphone", max_length=255)
    period = forms.CharField(label="Période", max_length=255)    
    message = forms.CharField(label="Message", max_length=2048, required=False, widget=forms.Textarea, help_text="Merci de préciser la taille du (ou des) cyclistes et le type de vélo souhaité.")

    def __init__(self, *args, **kwargs):
        super(BikeRentalForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        

    def get_success_url(self):
        return reverse('bike-rental')

    def form_valid(self, form):

        send_templated_mail(
                    template_name='contact',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    headers = {'Reply-To' : form.cleaned_data['email']},
                    context = {
                        'subject': 'Contact location — Global Vélo ',
                        'message': form.cleaned_data['message'],
                        'email': form.cleaned_data['email']
                    }
                )

        return super(BikeSell, self).form_valid(form)

class BikeRental(FormView):

    template_name = 'locations.html'

    form_class = BikeRentalForm
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

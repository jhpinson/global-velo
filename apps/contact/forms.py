# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from mail_templated.message import EmailMessage

from django import forms
from django.conf import settings
from crispy_forms.helper import FormHelper

class Contact(forms.Form):
    
    email = forms.EmailField(label='Adresse e-mail')
    subject = forms.CharField(label="Sujet", max_length=255)
    message = forms.CharField(label="Message", max_length=2048, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    def send_message(self):
        context = {
                        'subject': self.cleaned_data['subject'],
                        'message': self.cleaned_data['message'],
                        'email': self.cleaned_data['email']
                    }
        message = EmailMessage('templated_email/contact.html', context=context, headers = {'Reply-To' : self.cleaned_data['email']})
        message.from_email = settings.DEFAULT_FROM_EMAIL
        message.to = [settings.CONTACT_EMAIL]
        message.send()


class RentalContact(forms.Form):

    email = forms.EmailField(label='Adresse e-mail')
    phone = forms.CharField(label="Téléphone", max_length=255)
    period = forms.CharField(label="Période", max_length=255)
    message = forms.CharField(label="Message", max_length=2048, required=True, widget=forms.Textarea, help_text="Merci de préciser la taille du (ou des) cyclistes et le type de vélo souhaité.")

    def __init__(self, *args, **kwargs):
        super(RentalContact, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_tag = False

    def send_message(self):
        context = {
                        'message': self.cleaned_data['message'],
                        'email': self.cleaned_data['email'],
                        'phone' : self.cleaned_data['phone'],
                        'period' : self.cleaned_data['period'],
                    }
        message = EmailMessage('templated_email/rental-contact.html', context=context, headers = {'Reply-To' : self.cleaned_data['email']})
        message.from_email = settings.DEFAULT_FROM_EMAIL
        message.to = [settings.CONTACT_EMAIL]
        message.send()
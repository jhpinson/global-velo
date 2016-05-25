# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django import forms
from crispy_forms.helper import FormHelper

class Contact(forms.Form):
    
    email = forms.EmailField(label='Adresse e-mail')
    subject = forms.CharField(label="Sujet", max_length=255)
    message = forms.CharField(label="Message", max_length=2048, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        
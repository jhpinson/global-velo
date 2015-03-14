# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.conf import settings

from templated_email import send_templated_mail

from . import forms

class Contact(FormView):
    
    form_class = forms.Contact
    template_name = "contact/send.html"
    
    def get_success_url(self):
        return reverse('contact-sent')
    
    def form_valid(self, form):
        
        send_templated_mail(
                    template_name='contact',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    headers = {'Reply-To' : form.cleaned_data['email']},
                    context = {
                        'subject': form.cleaned_data['subject'],
                        'message': form.cleaned_data['message'],
                        'email': form.cleaned_data['email']
                    }
                )
        
        return super(Contact, self).form_valid(form)
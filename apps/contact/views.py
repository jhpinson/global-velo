# encoding: utf-8
from __future__ import unicode_literals, absolute_import

import json

from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.views.generic.edit import FormView
from django.conf import settings

from templated_email import send_templated_mail

from . import forms
from utils.ajax import serialize_form_errors

from pages.models import Page, Section
from partners.models import Partner

class Contact(FormView):

    form_class = forms.Contact
    template_name = "contact/send.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Contact, self).get_context_data(*args, **kwargs)
        section = Section.objects.get(pk=1)
        context['pages'] = Page.objects.filter(section=section, visible=True)
        context['partners'] = Partner.objects.filter(active=True)
        
        return context


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


class AjaxContact(Contact):

    def form_invalid(self, form):
        return HttpResponse(json.dumps({
            "success": False,
            "errors": serialize_form_errors(form)
        }), content_type='application/json')

    def form_valid(self, form):

        super(AjaxContact, self).form_valid(form)

        response = {'success' : True, 'reset' : True}

        return HttpResponse(json.dumps(response), content_type='application/json')


class ContactSent(Contact):

    def get_context_data(self, **kwargs):

        context = super(ContactSent, self).get_context_data(**kwargs)

        context['show_success_message'] = True

        return context
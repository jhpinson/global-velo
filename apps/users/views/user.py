# encoding: utf-8
from __future__ import unicode_literals, absolute_import

from class_based_auth_views.views import LoginView as LoginView_

from django.views.generic.edit import CreateView
from .. import forms
from .. import models
from django.contrib import messages
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.decorators.cache import never_cache

class CreateUser( CreateView):
    
    form_class = forms.UserCreationForm
    model = models.User
    template_name = "users/user_create.html"
    
    def get_form_kwargs(self):
        kwargs =super(CreateUser, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
        
        
    def get_success_url(self):
        return self.request.GET.get('next', '/')
    
    def form_valid(self, form):
        response = super(CreateUser, self).form_valid(form)
        self.object.backend = 'django.contrib.auth.backends.ModelBackend'
        login(self.request, self.object)
        messages.success(self.request, "Votre compte a été créé. ")
        return response

class Login( LoginView_):
    form_class = forms.Authentication
    template_name = "users/login.html"
    
    def get_success_url(self):
        return self.request.GET.get('next', '/')
    
    def get_form_kwargs(self):
        kwargs = super(Login, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    
class Logout(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect('/')
   
    
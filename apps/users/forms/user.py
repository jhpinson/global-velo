# encoding: utf-8
from __future__ import unicode_literals
from django import forms
from .. import models 
from crispy_forms.helper import FormHelper
from django.contrib.auth.forms import AuthenticationForm as AuthenticationForm_,\
    ReadOnlyPasswordHashField
from django.utils.translation import ugettext_lazy as _


class Authentication(AuthenticationForm_):
    
    def __init__(self, *args, **kwargs):
        
        request = kwargs.pop('request')
        
        super(Authentication, self).__init__( *args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        

class AdminUserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_email': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    email = forms.EmailField(label=_('Email'))
    
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = models.User
        fields = ("email",)

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        
        email = self.cleaned_data["email"]
        try:
            models.User._default_manager.get(email=email)
        except models.User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(AdminUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class AdminUserChangeForm(forms.ModelForm):
    email = forms.EmailField(label=_('Email'))
    
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = models.User
        exclude = ()
    def __init__(self, *args, **kwargs):
        super(AdminUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
        
class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    error_messages = {
        'duplicate_email': "Un utilisateur avec cette adresse email existe déjà",
        'password_mismatch': "Les mots de passe ne correspondent pas",
        'duplicate_username' : 'Un utilisateur avec ce pseudonyme existe déjà'
    }

    username = forms.CharField(label = 'Pseudonyme', max_length=30)

    email = forms.EmailField(label="Adresse email", max_length=75)
    
    password1 = forms.CharField(label="Mot de passe",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmation du mot de passe",
        widget=forms.PasswordInput,
        help_text="Veuillez saisir le même mot de passe que ci-dessus.")
    
    class Meta:
        model = models.User
        fields = ("email", "password1", "password2")

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            models.User._default_manager.get(email=email)
        except models.User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            models.User._default_manager.get(username__iexact=username)
        except models.User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


    def __init__(self, *args, **kwargs):
        
        request = kwargs.pop('request')
        
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
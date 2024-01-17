from django import forms
import re
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


from account.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50, help_text='Please enter a valid email address')
    class Meta:
        model = User
        fields = ("email", "username", "first_name", "last_name", "gender", "password1", "password2")
    def clean_first_name(self):
        firstname = self.cleaned_data['first_name']
        if not re.match("^[A-Za-z]+$", firstname):
            raise ValidationError('First name should only contain letters.')
        else:
            return firstname

    def clean_last_name(self):
        lastname = self.cleaned_data['last_name']
        if not re.match("^[A-Za-z]+$", lastname):
            raise ValidationError('Last name should only contain letters.')
        else:
            return lastname

class AuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Your password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'gender')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % email)
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nickname "%s" is already in use.' % username)

    def clean_first_name(self):
        firstname = self.cleaned_data['first_name']
        if not re.match("^[A-Za-z]+$", firstname):
            raise ValidationError('First name should only contain letters.')
        else:
            return firstname

    def clean_last_name(self):
        lastname = self.cleaned_data['last_name']
        if not re.match("^[A-Za-z]+$", lastname):
            raise ValidationError('Last name should only contain letters.')
        else:
            return lastname
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from .models import *
from django.contrib.auth.models import User
from django_countries.fields import CountryField

""" Registraion form """


class Registration_form(forms.Form):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'class': 'form_input'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'form_input'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class': 'form_input'}))
    email = forms.EmailField(label="Email-id", widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    mobileno = forms.CharField(max_length=10, label="Mobile_no", widget=forms.TextInput(attrs={'class': 'form_input'}))
    address = forms.CharField(label="Address", widget=forms.Textarea(attrs={'width': "100%", 'cols': "55", 'rows': "10", 'class': 'form_textarea'}))
    country = CountryField().formfield()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email


class login_form(forms.Form):
    email = forms.EmailField(label="Email-id", widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))


class Update_form(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['profile_image']

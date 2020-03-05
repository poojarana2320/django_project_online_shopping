from django import forms
from django.forms import ModelForm , TextInput , Textarea
from .models import *
from django.contrib.auth.models import User
# from django_countries.fields import CountryField
from django_countries.fields import CountryField
# from django_countries.fields import CountryField
# from django_countries import countries
# from django_countries.countries import COUNTRIES

country_choices=(
        ('india','India'),
        ('us','US'),
        ('canada','Canada'),
        ('australia','Australia'),
        ('spain','Spain'),
        ('japan','Japan')
        )
class Registration_form(forms.Form):
    username = forms.CharField(label="User_name",widget=forms.TextInput(attrs={'class': 'form_input'}))
    first_name = forms.CharField(label="First_name",widget=forms.TextInput(attrs={'class': 'form_input'}))
    last_name = forms.CharField(label="Last_name",widget=forms.TextInput(attrs={'class': 'form_input'}))
    email = forms.EmailField(label="Email_id", widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    mobileno = forms.CharField(label="Mobile_no",widget=forms.TextInput(attrs={'class': 'form_input'}))
    address = forms.CharField(label="Address",widget=forms.Textarea(attrs={'width':"100%", 'cols' : "55", 'rows': "10", 'class': 'form_textarea' }))
    country = CountryField().formfield()

   

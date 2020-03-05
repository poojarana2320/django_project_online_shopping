from django import forms
from . models import *
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','email','password')

class User_Login_form(forms.Form):
    username= forms.CharField(
       label="Username", widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    otp = forms .IntegerField(label="OTP", widget=forms.TextInput(attrs={'class': 'form_input'}))
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import os
from django_countries.fields import CountryField
from django_countries import countries

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class Registration(models.Model):
    # username=models.CharField(max_length=50)
    # fullname=models.CharField(max_length=50)
    # email=models.EmailField()
    # password=models.CharField(max_length=50)
    # confirmpassword=models.CharField(max_length=50)
    user_id=models.OneToOneField(User)
    mobileno=models.IntegerField()
    address=models.TextField(max_length=50)
    country_choices=(
        ('india','India'),
        ('us','US'),
        ('canada','Canada'),
        ('australia','Australia'),
        ('spain','Spain'),
        ('japan','Japan')
        )
    # country=models.CharField(choices=country_choices,max_length=10)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    country = CountryField(choices=list(countries))

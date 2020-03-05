from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,related_name="user_id")
    otp=models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


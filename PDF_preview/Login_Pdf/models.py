from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

"""Signup table """

def validate_file_extension(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError(u'Error message')

class Signup(models.Model):
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	upload_file = models.FileField(upload_to="files/", blank=True, null=True,validators=[validate_file_extension]) 

	def __str__(self):
		return self.user_id.username 
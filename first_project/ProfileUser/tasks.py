from __future__ import absolute_import
import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def login_form(email):
	send_mail(
            'Login',
            'Successfully Logged In',
            'pooja.rana@ia.ooo',
            ['to@example.com'],
            fail_silently=False,
        )
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-28 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProfileUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='OTP',
            new_name='otp',
        ),
    ]

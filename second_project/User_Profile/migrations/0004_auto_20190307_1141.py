# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-07 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0003_auto_20190306_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
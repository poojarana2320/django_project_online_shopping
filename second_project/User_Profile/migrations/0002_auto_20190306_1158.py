# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-06 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mobileno',
            field=models.IntegerField(max_length=10),
        ),
    ]

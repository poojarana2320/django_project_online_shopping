# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-11 04:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0009_auto_20190311_0419'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping_Cart',
            new_name='Product',
        ),
    ]

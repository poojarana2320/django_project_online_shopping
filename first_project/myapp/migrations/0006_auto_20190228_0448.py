# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-28 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20190228_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant_review',
            old_name='Name',
            new_name='name',
        ),
    ]

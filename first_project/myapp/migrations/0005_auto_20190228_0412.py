# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-28 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20190227_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingairticket',
            name='Travel_From_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='bookingairticket',
            name='Travel_To_Date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

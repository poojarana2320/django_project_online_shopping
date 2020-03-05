# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-06 04:49
from __future__ import unicode_literals

import User_Profile.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.IntegerField()),
                ('address', models.TextField(max_length=50)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=User_Profile.models.get_image_path)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-05 10:20
from __future__ import unicode_literals

import UserProfile.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserProfile', '0003_delete_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.IntegerField()),
                ('address', models.TextField(max_length=50)),
                ('country', models.CharField(choices=[('india', 'India'), ('us', 'US'), ('canada', 'Canada'), ('australia', 'Australia'), ('spain', 'Spain'), ('japan', 'Japan')], max_length=10)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=UserProfile.models.get_image_path)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

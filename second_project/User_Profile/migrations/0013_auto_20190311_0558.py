# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-11 05:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_Profile', '0012_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
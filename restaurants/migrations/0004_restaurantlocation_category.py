# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-08 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20180308_0604'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

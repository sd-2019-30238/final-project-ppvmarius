# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-07 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0002_auto_20190607_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='delivered',
            field=models.CharField(default=b'no', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='driver',
            field=models.CharField(default=b'no', max_length=50),
            preserve_default=False,
        ),
    ]

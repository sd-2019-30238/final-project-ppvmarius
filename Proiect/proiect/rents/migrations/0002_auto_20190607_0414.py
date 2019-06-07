# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-07 01:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rent',
            name='endDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rent',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 7, 1, 14, 1, 848000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

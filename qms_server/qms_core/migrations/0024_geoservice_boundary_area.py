# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-09-21 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qms_core', '0023_auto_20170628_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='geoservice',
            name='boundary_area',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

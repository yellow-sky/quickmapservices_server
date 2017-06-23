# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-23 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qms_core', '0019_auto_20170621_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoservice',
            name='last_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='last_for', to='qms_core.GeoServiceStatus'),
        ),
    ]

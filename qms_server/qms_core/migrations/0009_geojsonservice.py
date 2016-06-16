# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qms_core', '0008_wfsservice_layer'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoJsonService',
            fields=[
                ('geoservice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='qms_core.GeoService')),
                ('url', models.URLField()),
            ],
            bases=('qms_core.geoservice',),
        ),
    ]
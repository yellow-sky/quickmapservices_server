# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qms_core', '0010_auto_20160422_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wfsservice',
            name='layer',
            field=models.CharField(max_length=1024, verbose_name='Layer name ([namespace:]featuretype)'),
        ),
    ]

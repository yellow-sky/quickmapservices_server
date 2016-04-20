# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import qms_core.size_restricted_image_field


class Migration(migrations.Migration):

    dependencies = [
        ('qms_core', '0005_geoservice_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceicon',
            name='icon',
            field=qms_core.size_restricted_image_field.SizeRestrictedImageField(max_length=200, upload_to='service_icon/', verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='serviceicon',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='icon name'),
        ),
    ]
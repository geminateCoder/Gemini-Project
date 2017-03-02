# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import timezone_field.fields
import userprofile.models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=userprofile.models.upload_location),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='Europe/London'),
        ),
    ]

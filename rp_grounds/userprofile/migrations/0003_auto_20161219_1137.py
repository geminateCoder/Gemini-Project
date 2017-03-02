# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 16:37
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_auto_20161219_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default=django.utils.timezone.now),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='staff',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

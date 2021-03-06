# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-23 04:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20161222_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='length',
        ),
        migrations.AddField(
            model_name='post',
            name='pref',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Male', 'Male'), ('Female', 'Female'), ('FTM', 'FTM'), ('MTF', 'MTF')], max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.TextField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('Fandom', 'Fandom'), ('Fantasy/Supernatural', 'Fantasy/Supernatural'), ('Historical', 'Historical'), ('Sci-Fi', 'Sci-Fi'), ('Slice of Life', 'Slice of Life'), ('Romance', 'Romance'), ('Horror', 'Horror'), ('Mystery', 'Mystery'), ('Steampunk', 'Steampunk'), ('Cyberpunk', 'Cyberpunk'), ('Victorian Era', 'Victorian Era'), ('Drama', 'Drama')], default='Select Genre', max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='max_height',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='max_width',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(500), django.core.validators.MinValueValidator(500)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='rptype',
            field=models.CharField(choices=[('SFW', 'SFW'), ('NSFW', 'NSFW'), ('NSFW-EXTREME', 'NSFW-EXTREME')], default='SFW', max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='style',
            field=models.CharField(choices=[('Script', 'Script'), ('Para', 'Para'), ('Novel', 'Novel')], default='Select a Style', max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(blank=True, choices=[('Blog', 'Blog'), ('Prompt', 'Prompt'), ('Fanfiction', 'Fanfiction')], max_length=64, null=True),
        ),
    ]

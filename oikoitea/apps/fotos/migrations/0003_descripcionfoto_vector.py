# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-28 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0002_auto_20170916_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcionfoto',
            name='vector',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

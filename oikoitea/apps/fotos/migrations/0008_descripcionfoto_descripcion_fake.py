# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-15 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0007_descripcionfoto_sinonimos'),
    ]

    operations = [
        migrations.AddField(
            model_name='descripcionfoto',
            name='descripcion_fake',
            field=models.TextField(default='', max_length=999),
        ),
    ]

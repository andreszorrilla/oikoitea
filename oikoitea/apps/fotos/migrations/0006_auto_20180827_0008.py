# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-27 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotos', '0005_auto_20180427_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descripcionfoto',
            name='descripcion',
            field=models.TextField(default='', max_length=999),
        ),
    ]
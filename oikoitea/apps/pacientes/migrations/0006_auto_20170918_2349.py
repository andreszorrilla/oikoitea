# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 23:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0005_auto_20170916_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date(2017, 9, 18)),
        ),
    ]

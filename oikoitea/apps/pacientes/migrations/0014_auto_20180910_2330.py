# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-09-10 23:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0013_auto_20180827_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name=b'fecha_nacimiento',
            field=models.DateField(default=datetime.date(2018, 9, 10)),
        ),
    ]

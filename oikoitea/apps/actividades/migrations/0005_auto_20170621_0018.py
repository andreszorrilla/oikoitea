# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_auto_20170612_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividaddetalle',
            name='estado',
            field=models.CharField(choices=[('SE', 'Sin Estado'), ('AC', 'Estado Actual'), ('LO', 'Bien'), ('NL', 'Mal'), ('IN', 'No valido')], default='SE', max_length=2),
        ),
        migrations.AlterField(
            model_name='actividad',
            name='descripcion',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]

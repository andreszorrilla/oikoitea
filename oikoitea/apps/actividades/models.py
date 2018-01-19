# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.db import models


def photo_path(instance, filename):
    return 'actividades/imagen_{0}{1}'.format(instance.id, ".png")


class Actividad(models.Model):
    nombre      = models.CharField(max_length=20, default="")
    descripcion = models.CharField(max_length=50, default="", blank=True)

    def __str__(self):
        return self.descripcion

    def get_absolute_url(self):
        return reverse('actividad:actividades_index')

    @models.permalink
    def get_success_url(self):
        return reverse('actividad:actividades_index')

    def actividades_detalles(self):
        return ActividadDetalle.objects.filter(actividad_id=self.id)


class ActividadDetalle(models.Model):
    db_table = 'actividad_detalle'
    actividad   = models.ForeignKey(Actividad)
    descripcion = models.CharField(max_length=20, default="")
    imagen      = models.ImageField(upload_to=photo_path, blank=True)

    SIN_ESTADO  = 'SE'
    ACTUAL      = 'AC'
    LOGRADO     = 'LO'
    NO_LOGRADO  = 'NL'
    INVALIDO    = 'IN'
    ESTADO_CHOICES = (
        (SIN_ESTADO, 'Sin Estado'),
        (ACTUAL, 'Estado Actual'),
        (LOGRADO, 'Bien'),
        (NO_LOGRADO, 'Mal'),
        (INVALIDO, 'No valido'),
    )
    estado = models.CharField(
        max_length=2,
        choices=ESTADO_CHOICES,
        default=SIN_ESTADO
    )

    def get_glyphicon(self):
        estados = {
                    'SE': '',
                    'AC': 'glyphicon-arrow-up',
                    'LO': 'glyphicon-ok',
                    'NL': 'glyphicon-remove',
                    'IN': 'glyphicon-ban-circle'
                  }
        return estados[self.estado]



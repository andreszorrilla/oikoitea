# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import reverse
from django.db import models


class Foto(models.Model):
    nombre_archivo = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nombre_archivo

    def descripciones_fotos(self):
    	descripciones = DescripcionFoto.objects.filter(foto=self)
    	return descripciones


class DescripcionFoto(models.Model):
    db_table = 'actividad_detalle'
    foto        = models.ForeignKey(Foto)
    descripcion = models.TextField(max_length=1000, default="")
    #vector      = models.TextField()


    def __str__(self):
        return self.descripcion

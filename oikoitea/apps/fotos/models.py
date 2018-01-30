# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import reverse
from django.db import models
import jsonpickle
import numpy as np


class Foto(models.Model):
    nombre_archivo = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.nombre_archivo

    def descripciones_fotos(self):
    	descripciones = DescripcionFoto.objects.filter(foto=self)
    	return descripciones


class DescripcionFoto(models.Model):
    db_table = 'actividad_detalle'
    foto        = models.ForeignKey(Foto, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=1000, default="")
    vector      = models.TextField()


    def __str__(self):
        return self.descripcion

    @classmethod
    def new_with_components(cls, foto, descripcion, vector):
        foto_descripcion = cls(foto=foto, descripcion=descripcion)
        foto_descripcion.encode_vector(vector)
        return foto_descripcion

    def encode_vector(self, vector):
        self.vector = jsonpickle.encode(vector.tolist())

    def decode_vector(self):
        vector = jsonpickle.decode(self.vector)
        return np.array(vector)

    @staticmethod
    def avg_sentence(sentence, wv):
        v = np.zeros(300)
        for w in sentence:
            if w in wv:
                v += wv[w]
        return v / len(sentence)

# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.urls import reverse
from django.db import models
import jsonpickle
import numpy as np


class Foto(models.Model):
    nombre_archivo = models.TextField()

    def __str__(self):
        return self.nombre_archivo

    def descripciones_fotos(self):
    	descripciones = DescripcionFoto.objects.filter(foto=self)
    	return descripciones

    @staticmethod
    def get_by_descripcion(descripcion):
        input_average = DescripcionFoto.avg_feature_vector(descripcion, model=model, num_features=300, index2word_set=index2word_set)




class DescripcionFoto(models.Model):
    db_table = 'actividad_detalle'
    foto        = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name="+",)
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

    @staticmethod
    def avg_feature_vector(sentence, model, num_features, index2word_set):
        words = sentence.split()
        feature_vec = np.zeros((num_features, ), dtype='float32')
        n_words = 0
        for word in words:
            if word in index2word_set:
                n_words += 1
                feature_vec = np.add(feature_vec, model[word])
        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        return feature_vec

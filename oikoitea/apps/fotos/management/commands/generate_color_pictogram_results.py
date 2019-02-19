# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from apps.fotos.models import Foto, DescripcionFoto

import re
import urllib, json
from gensim.models import Word2Vec
import gensim
import sys
import numpy as np

from pprint import pprint  # pretty-printer
from heapq import *


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)




"""
SI FALLA CARGAR DB POR PROBLEMA DE UTF-8

use oikoitea_flirck30k;

ALTER TABLE fotos_foto MODIFY COLUMN nombre_archivo LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

ALTER TABLE fotos_descripcionfoto MODIFY COLUMN sinonimos LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';


"""


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))



class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    @staticmethod
    def generar_lista():
        filename = "/home/andres/Dropbox/Tesis/oikoitea.git/oikoitea/scripts/traducciones/flickr30k.txt"
        limit = 20
        count = 0
        ultimo_texto = ''
        foto = None
        lista_oraciones = []
        with open(filename) as f:
            for line in f:
                str_split = re.compile("^(\d+\.jpg)#(\d)\s+(.+)").split(line)
                nombre_archivo  = str_split[1]
                numero_texto    = str_split[2]
                descripcion     = str_split[3]
                if ultimo_texto != nombre_archivo:
                    count += 1
                descripcion = descripcion.strip()
                lista_oraciones.append( (nombre_archivo, descripcion) )
                ultimo_texto = nombre_archivo
                if limit == 0:
                    break
        return lista_oraciones



    def cosine_sim(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        # Preparamos dos arreglos, una para la "base de datos" y la otra para las "consultas"
        arr_db = []
        arr_query = []

        # Cargamos las fotos

        fotos = Foto.objects.using('oikoitea_flirck30k').all()[:1000]
        for foto in fotos:
            descripciones = list(DescripcionFoto.objects.using('oikoitea_flirck30k').filter(foto=foto))[:-1]

            for descr_db in descripciones:
                elem = (descr_db.decode_vector(), descr_db.descripcion, descr_db.foto)
                arr_db.append( elem )

            elem_last = descripciones[-1]
            elem_query = (elem_last.decode_vector(), elem_last.descripcion, elem_last.foto)
            arr_query.append( elem_query )

        print( len(arr_db) )
        print( len(arr_query) )

        # Recorremos cada una de las consultas, consultando su similaridad

        sum_aciertos = 0
        for query in arr_query:
            query_vector, query_descripcion, query_foto = query
            h = []
            for db in arr_db:
                db_vector, db_descripcion, db_foto = db
                heappush(h, (cosine_sim(query_vector, db_vector), (db_descripcion, db_foto) ))

            aciertos = 0
            iteraciones = 0
            for elem in nlargest(10, h):
                sim, (descripcion, foto) = elem
                if foto.nombre_archivo == query_foto.nombre_archivo:
                    aciertos += 1
                iteraciones += 1

            sum_aciertos += (aciertos / 4.0)
            print "Aciertos: ", aciertos, "Esperado: ", 4,  "Profundidad: ", iteraciones, "\tPorcentaje", (aciertos / 4.0)

        print "Suma de aciertos: ", (sum_aciertos / len(arr_query) * 1.0)
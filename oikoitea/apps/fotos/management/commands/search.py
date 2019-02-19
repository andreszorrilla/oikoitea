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

use oikoitea_development_pictogramas;

ALTER TABLE fotos_foto MODIFY COLUMN nombre_archivo LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

ALTER TABLE fotos_descripcionfoto MODIFY COLUMN descripcion LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';


"""



"""
    Este script mide la precision del algoritmo con la base de datos de flickr ...

"""


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def avg_sentence(sentence, wv):
    v = np.zeros(300)
    for w in sentence:
        if w in wv:
            v += wv[w]
    return v / len(sentence)


import numpy as np
from scipy import spatial


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

    def avg_sentence(sentence, wv):
        v = np.zeros(300)
        for w in sentence:
            if w in wv:
                v += wv[w]
        return v / len(sentence)


#    def add_arguments(self, parser):
#        parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'

        model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)

        index2word_set = set(model.index2word)

    
        # Preparamos dos arreglos, una para la "base de datos" y la otra para las "consultas"
        arr_db = []

        # Cargamos las fotos
        fotos = Foto.objects.all()
        for foto in fotos:
            descripciones = list(DescripcionFoto.objects.filter(foto=foto))

            for descr_db in descripciones:
                vector = avg_feature_vector(descr_db.descripcion, model=model, num_features=300, index2word_set=index2word_set)
                # vector = descr_db.decode_vector()
                elem = (vector, descr_db.descripcion, descr_db.foto)
                arr_db.append( elem )

        #url_descr = generar_lista()
        # avgs = list(map(lambda p: p + (avg_sentence(p[1].split(), model.wv),), url_descr))

        while True:
            text = raw_input("Ingrese texto (q! para salir): ")
            if text == "q!":
                sys.exit(0)

            #inputv = avg_sentence(text.split(), model.wv)
            inputv = avg_feature_vector(text, model=model, num_features=300, index2word_set=index2word_set)
            #sims = list(map(lambda p: p[:2] + (cosine_sim(inputv, p[0]),), arr_db))
            h = []
            for av in arr_db:
                #cosine = cosine_sim(inputv, av[0])
                cosine = spatial.distance.cosine(inputv, av[0])
                heappush(h, (cosine, av[1]) )
            

            print len(arr_db)

            for elem in nlargest(15, h):
                print(elem[0], elem[1])

            print("***************")

            for elem in nsmallest(15, h):
                print(elem[0], elem[1])
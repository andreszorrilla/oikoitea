# -*- encoding: utf-8 -*-

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



import numpy as np
from scipy import spatial

#from thesaurus import Word



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


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'




    

    def handle(self, *args, **options):
        filename = "/home/andres/Desktop/datasetNLG.txt"

        W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)
        index2word_set = set(model.index2word)


        arr_db    = []
        arr_query = []
        count = 0

#       
        with open(filename) as f:
            for line in f:
                #print line.split("|")
                bd, query = line.split("|")
                vector_bd    = avg_feature_vector(bd, model=model, num_features=300, index2word_set=index2word_set)
                vector_query = avg_feature_vector(query, model=model, num_features=300, index2word_set=index2word_set)

                arr_db.append(    (vector_bd, bd, count) )
                arr_query.append( (vector_query, query, count) )

                count += 1

        profundidades = [2, 4, 7, 10]
        for profundidad in profundidades:
            sum_aciertos = 0
            for query in arr_query:
                query_vector, query_descripcion, query_foto = query
                h = []
                for db in arr_db:
                    db_vector, db_descripcion, db_foto = db
                    #cosine = cosine_sim(query_vector, db_vector)
                    cosine = 1 - spatial.distance.cosine(query_vector, db_vector)
                    heappush(h, (cosine, (db_descripcion, db_foto) ))

                aciertos = 0
                iteraciones = 0
                for elem in nlargest(profundidad, h):
                    sim, (descripcion, foto) = elem
                    if foto == query_foto:
                        aciertos += 1
                    iteraciones += 1

                sum_aciertos += (aciertos * 100) 
                #print "Aciertos: ", aciertos, "Esperado: ", 1,  "Profundidad: ", iteraciones, "\tPorcentaje", (aciertos * 100)
            print ""
            print "Profundidad: ", profundidad
            print "Suma de aciertos: ", sum_aciertos
            print "Cantidad: ", len(arr_query)
            print "Precision: ", 1.0 * sum_aciertos / len(arr_query)
            print ""





















#    def handle(self, *args, **options):
#        filename = "/home/andres/names.txt"
#        from thesaurus import Word
#        with open(filename) as f:
#            for line in f:
#                palabras = line.strip().split(" ")
#                if len(palabras) == 1:
#                    syns = Word(palabras[0]).synonyms()
#                    print palabras[0], "=", "(",
#                    for s in syns:
#                        print s, ",",
#                    print ")"
#                if len(palabras) > 1:
#                    for p in palabras:
#                        pass


#    ##   Ejemplo simple de llamada a las APis de Apicultur desde python 
#    ##   Sólo sirve para ver como se hacen las llamdas, y como se seleccionan algunos valores
#    ##  de la respuesta. [se devuelve una lista pero sólo se sacan valores de la primera palabra y el primer
#    ##  lema de la lista]
#    ##   IMPORTANTE: Debes colocar el valor del Access Token para que funcione!  
#    ##  necesitas instalar el modulo requests y el modulo JSON 


#    import requests
#    import json

#    ## IMPORTANTE: PON EL VALOR DE TU ACCESS TOKEN

#    ACCESS_TOKEN = 'dQfoyj0ZfT3cj01PnOuKJ4XCFVIa'

#    ## La función que llama a las APIs

#    def apicultur_get(query,endpoint):

#    ## Info de los headers, respuesta en JSON y clave de acceso: Recuerda cambiarla

#        headers = {'content-type': 'application/json', 'Authorization':'Bearer '+ ACCESS_TOKEN}

#        r = requests.get( endpoint+query,  headers=headers)

#        if r.status_code == 200:
#            results = r.json()
#            print 'Objeto JSON devuelto por la API( en este caso es una lista):'
#            print results
#            return (results)
#        else:
#            print 'respuesta erronea, codigo de error', r.status_code, 'valor devuelto'#, r.json()
#            return False


#
#    """
#    SI FALLA CARGAR DB POR PROBLEMA DE UTF-8

#    use oikoitea_flirck30k;

#    ALTER TABLE fotos_foto MODIFY COLUMN nombre_archivo LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

#    ALTER TABLE fotos_descripcionfoto MODIFY COLUMN descripcion LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

#    SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';

#    """
#    class Command(BaseCommand):
#        help = 'Closes the specified poll for voting'

#        def handle(self, *args, **options):
#            descripciones = DescripcionFoto.objects.all()[10:]
#            for desc in descripciones:
#                print desc.descripcion
#                ## Este es el inicio del programa:
#                ## en primer lugar ponemos la dirección del end point
#                ## Y después el valor que pasamos
#                ## endpoint + query es la llamada que haremos
#
#                endpoint = "http://store.apicultur.com/api/categoriza/1.0.0/"
#                query = desc.descripcion
#
#                response = apicultur_get(query,endpoint)
#                if response != False:
#                    print 'Datos palabra a procesar (elemento del diccionario): ', response['categorias']  
#                    print
#                    print 'Valor del campo palabra [diccionario]:', response['palabra']
#                    print
#                    print 'Valor del primer valor de las categorias', response['categorias'][0]
#                    print
#                    print 'Valor del segundo valor de las categorias', response['categorias'][1]
#                    print
#
#                else:
#                       print "Respuesta errónea", query
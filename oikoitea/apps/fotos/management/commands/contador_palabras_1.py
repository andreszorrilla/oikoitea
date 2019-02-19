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
        #filename = "/home/andres/Desktop/datasetNLG.txt"
        filename = "/home/andres/Dropbox/Tesis/oikoitea.git/oikoitea/scripts/traducciones/datasetNLG.txt"

        W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)
        index2word_set = set(model.index2word)



        set_total_palabras = set()
        set_palabras_fuera_del_vocabulario = set()

#       
        with open(filename) as f:
            for line in f:
                #print line.split("|")
                words = line.split(" ")
                
                for word in words:
                    if not word in set_total_palabras:
                        set_total_palabras.add( word )
                    
                        if word in index2word_set:
                            set_palabras_fuera_del_vocabulario.add( word.lower() )

            print len(set_total_palabras)
            print "*************"
            print len(set_palabras_fuera_del_vocabulario)



        filename = "/home/andres/Dropbox/Tesis/oikoitea.git/oikoitea/scripts/traducciones/flickr30k_to_train.txt"



#       
        with open(filename) as f:
            for line in f:
                #print line.split("|")
                words = line.split(" ")
                
                for word in words:
                    if not word in set_total_palabras:
                        set_total_palabras.add( word )
                    
                        if word in index2word_set:
                            set_palabras_fuera_del_vocabulario.add( word.lower() )

            print len(set_total_palabras)
            print "*************"
            print len(set_palabras_fuera_del_vocabulario)



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

import numpy as np
from scipy import spatial


"""
    

"""


def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


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

    def handle(self, *args, **options):

        # A VECTOR SPACE MODEL is loaded
        W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'
        model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)
        index2word_set = set(model.index2word)

        # A Bag of word is created
        # Every word from the bag of word is vectorized and pushed into a list
        BAG_OF_WORDS = ["cat", "dog",  "dalmata", "German shepherd", "pitbull", "animal", "red", "person", "car", "cycle", "walk", "chicken"]
        VECTORIZED_BAG_OF_WORDS = list(
                                    map(
                                        lambda text: (text.lower(), avg_feature_vector(text, model=model, num_features=300, index2word_set=index2word_set)),
                                        BAG_OF_WORDS
                                        )
                                    )

        # While the word inputted is not "quit"
        # it is vectorized and compared with all the VECTORIZED_BAG_OF_WORDS vectors
        # and finally sorted using a priority queue (heap)

        while True:
            text = raw_input("Enter a word (q! to exit): ")
            if text == "q!":
                sys.exit(0)

            input_word = avg_feature_vector(text, model=model, num_features=300, index2word_set=index2word_set)

            heap = []
            for averaged_words in VECTORIZED_BAG_OF_WORDS:
                cosine = spatial.distance.cosine(input_word, averaged_words[1])
                heappush(heap, (cosine, averaged_words[0]) )



            for elem in nlargest(15, heap):
                print(elem[0], elem[1])
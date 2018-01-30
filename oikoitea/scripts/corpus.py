# -*- coding: utf-8 -*-


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



import re
import urllib, json


from gensim.models import Word2Vec





def generar_lista():
    filename = "Dropbox/Tesis/oikoitea.git/oikoitea/scripts/traducciones/token-espanhol.txt"

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






def obtener_oraciones():
	filename = "/home/andres/Dropbox/oikoitea/scripts/traducciones/token-espanhol.txt"

	limit = 20
	count = 0

	ultimo_texto = ''

	foto = None

	lista_oraciones = []

	with open(filename) as f:
		for line in f:
			str_split = re.compile("^(\d+\.jpg)#(\d)\s+(.+)").split(line)

			nombre_archivo 	= str_split[1]
			numero_texto 	= str_split[2]
			descripcion		= str_split[3]


			descripcion = descripcion.decode("utf-8")
			
			if ultimo_texto != nombre_archivo:
				#print "\n", nombre_archivo
				count += 1

			#print descripcion

			descripcion = descripcion.strip()
			lista_oraciones.append( descripcion.split() )
			
			ultimo_texto = nombre_archivo

			if limit == 0:
				break

	return lista_oraciones



#############


import gensim

import sys
import numpy as np


from pprint import pprint  # pretty-printer
from heapq import *

W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'





def avg_sentence(sentence, wv):
    v = np.zeros(300)
    for w in sentence:
        if w in wv:
            v += wv[w]
    return v / len(sentence)

def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))






url_descr = generar_lista()


#model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
#model.build_vocab(obtener_oraciones())  # can be a non-repeatable, 1-pass generator

model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)




avgs = list(map(lambda p: p + (avg_sentence(p[1].split(), model.wv),), url_descr))

for a in avgs:
    print(a)
    sys.exit(0)


while True:

    text = raw_input("Ingrese texto (q! para salir): ")


    if text == "q!":
        sys.exit(0)

    inputv = avg_sentence(text.split(), model.wv)

    #   sims = list(
    #               map(
    #                   lambda p: (cosine_sim(inputv, p[2]), p[:2]) ,
    #               avgs)


    sims = list(map(lambda p: p[:2] + (cosine_sim(inputv, p[2]),), avgs))

    h = []
    for av in avgs:
        heappush(h, (cosine_sim(inputv, av[2]), (av[:2])) )

    for elem in nlargest(10, h):
        print(elem)

#   most_similar_meme = sorted(sims, key=lambda p: p[2], reverse=True)

#    for i in xrange(10):
#        print(most_similar_meme[i][2], " --> ", most_similar_meme[i][0], most_similar_meme[i][1])


    print("")





import numpy as np
from scipy import spatial

index2word_set = set(model.index2word)

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


s1_afv = avg_feature_vector('Un dia soleado en la playa', model=model, num_features=300, index2word_set=index2word_set)
s2_afv = avg_feature_vector('Agua mar, playa, sol y dia', model=model, num_features=300, index2word_set=index2word_set)
sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
print(sim)

#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import re

import gensim

import sys
import numpy as np


import jsonpickle

import numpy as np
from scipy import spatial
from heapq import heappush, heappop, heapify


from django.core.management.base import BaseCommand, CommandError
from apps.fotos.models import Foto, DescripcionFoto



from django.conf import settings






images_path = "/home/andres/Documents/tesis/images/Realista_completo"
files = [ join(images_path, f) for f in listdir(images_path) if isfile(join(images_path, f)) ]


hash_cosas = {}
hash_cosas['а'] = "a"
hash_cosas['В'] = "e"
hash_cosas['б'] = "i"
hash_cosas['в'] = "o"
hash_cosas['г'] = "u"
hash_cosas['д'] = "ñ"
hash_cosas['Б'] = 'ü'


def save_to_file():

	url_descr = []

	file = open(images_path + "/nombres.txt", "w") 
	for nombre_archivo in files:

		nombre_formateado = nombre_archivo.replace(images_path + "/", "")
		#Eliminamos guion bajo con numero
		nombre_formateado = re.sub("_\d*", "", nombre_formateado)
		nombre_formateado = re.sub("\.\/", "", nombre_formateado)
		nombre_formateado = re.sub("\.(jpg|png)", "", nombre_formateado)

		for k in hash_cosas:
			if k in nombre_formateado:
				v = hash_cosas[k]
				nombre_formateado = nombre_formateado.replace(k, v)

		line = "{0};{1}".format(nombre_archivo, nombre_formateado)
		file.write(line)
		file.write( "\n" )

		url_descr.append((nombre_archivo, nombre_formateado))

	file.close()



url_descr = []

save_to_file()
with open(images_path + "/nombres.txt") as f:
	for line in f:
		dir_archivo, descripcion = line.strip().split(";")

		url_descr.append( (dir_archivo, descripcion) )





W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'


#model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)
#model.train(obtener_oraciones())


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)










###################################################

index2word_set = set(model.index2word)

#
#s1_afv = DescripcionFoto.avg_feature_vector('this is a sentence', model=model, num_features=300, index2word_set=index2word_set)
#s2_afv = DescripcionFoto.avg_feature_vector('this is also sentence', model=model, num_features=300, index2word_set=index2word_set)
#sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
#print(sim)

averages = list(map(lambda p: p + (DescripcionFoto.avg_feature_vector(p[1], model=model, num_features=300, index2word_set=index2word_set) ,), url_descr))


DescripcionFoto.objects.all().delete()
Foto.objects.all().delete()

for av in averages:
	dir_archivo, descripcion_str, vector = av

	dir_archivo = dir_archivo.replace(settings.PICTOGRAMS_PATH, "")

	print dir_archivo

	foto = Foto(nombre_archivo=dir_archivo)
	foto.save()

	descripcion = DescripcionFoto.new_with_components(foto, descripcion_str, vector)
	descripcion.save()




sys.exit(0)


heap = []


while True:
	text = raw_input("Ingrese texto (q! para salir): ")

	if text == "q!":
		sys.exit(0)

	input_average = DescripcionFoto.avg_feature_vector(text, model=model, num_features=300, index2word_set=index2word_set)


	sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)

	#similarities = list(map(lambda p: p[:2] + (1 - spatial.distance.cosine(input_average, p[2]) ,), averages))
	#most_similar_meme = sorted(similarities, key=lambda p: p[2], reverse=True)

	for av in averages:
		similarity = spatial.distance.cosine(input_average, av[2])
		heap.append((similarity, av[:2]))

	heapify(heap)

	count = 50
	for item in heap:
		#item 					= heappop(heap)
		cosine_sim 				= item[0]
		dir_imagen, descripcion = item[1]
		print "{0}\t{1}\t{2}".format(cosine_sim, dir_imagen, descripcion)

		if (count == 0):
			sys.exit(0)

		count -= 1


sys.exit(0)
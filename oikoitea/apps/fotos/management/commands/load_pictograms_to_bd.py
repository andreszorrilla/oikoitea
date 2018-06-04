#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
import re
import gensim

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.fotos.models import Foto, DescripcionFoto


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'



    def format_name(self, name):
        nombre_formateado = re.sub("_\d*", "", name)
        nombre_formateado = re.sub("\.\/", "", nombre_formateado)
        nombre_formateado = re.sub("\.(jpg|png)", "", nombre_formateado)
        return nombre_formateado


    def handle(self, *args, **options):

        images_path = settings.PICTOGRAMS_PATH
        
        url_descr = []

        list_directories = [ (f, os.path.join(images_path, f)) for f in os.listdir(images_path) if os.path.isdir(os.path.join(images_path, f)) ]
        for image_dir_name, directory in list_directories:
            images = [(self.format_name(f), os.path.join(image_dir_name, f)) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

            for name, directory in images:
                url_descr.append( (directory, name) ) 



        #DescripcionFoto.objects.all().delete()
        #Foto.objects.all().delete()







        W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'

        #model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)
        #model.train(obtener_oraciones())


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






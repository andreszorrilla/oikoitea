# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from apps.fotos.models import Foto, DescripcionFoto

import re
import urllib, json
from gensim.models import Word2Vec
import gensim
import sys
import numpy as np



import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


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
        #self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))

        #model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
        #model.build_vocab(obtener_oraciones())  # can be a non-repeatable, 1-pass generator


        W2V_PATH = '/home/andres/Documents/tesis/modelos_esp/sbw_vectors.bin'

        model = gensim.models.KeyedVectors.load_word2vec_format(W2V_PATH, binary=True)

        url_descr = self.generar_lista()

        avgs = list(
                    map(
                        lambda p: p + (DescripcionFoto.avg_sentence(p[1].split(), model.wv),),
                    url_descr)
                )
        foto = None
        last_photo_name = ''
        for a in avgs:
            photo_name, description, vector = a
            print description

            if photo_name != last_photo_name:
                foto = Foto(nombre_archivo=photo_name)
                foto.save()

            i = DescripcionFoto.new_with_components(foto, description, vector)
            #print(a)
            #print("\n##################\n")
            #print( i.decode_vector(), type(i.vector), type(i.decode_vector()) )
            #sys.exit(0)



#
#
#
#        x = model.wv.similar_by_word('perro', topn=5)
#        print("\n----------------------\n")
#        print(x)
#        print("\n----------------------\n")
#
#        sys.exit(0)
#
#        avgs = list(
#                    map(
#                        lambda p: p + (DescripcionFoto.avg_sentence(p[1].split(), model.wv),),
#                    url_descr)
#                )
#        for a in avgs:
#            i = DescripcionFoto.new_with_components(None, a[1], a[2])
#            print(a)
#            print("\n##################\n")
#            print( i.decode_vector(), type(i.vector), type(i.decode_vector()) )
#            sys.exit(0)

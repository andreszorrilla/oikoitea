# -*- coding: utf-8 -*-

import re
import sys

import urllib, json


from apps.fotos.models import Foto, DescripcionFoto






"""
SI FALLA CARGAR DB POR PROBLEMA DE UTF-8

use oikoitea_development;
ALTER TABLE fotos_descripcionfoto MODIFY COLUMN descripcion LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';


"""

def cargar_bd():
	filename = "/home/andres/Dropbox/oikoitea/scripts/traducciones/token-espanhol.txt"

	limit = 20
	count = 0

	ultimo_texto = ''


	#file_output = open("/home/andres/Dropbox/oikoitea/scripts/traducciones/text-formatted3.txt", "a") 

	#translator = Translator(to_lang="es")

	last = "1000092795.jpg"
	found = True


	foto = None

	with open(filename) as f:
		for line in f:
			str_split = re.compile("^(\d+\.jpg)#(\d)\s+(.+)").split(line)

			nombre_archivo 	= str_split[1]
			numero_texto 	= str_split[2]
			descripcion		= str_split[3]
			
			if found:
				if ultimo_texto != nombre_archivo:
					print "\n", nombre_archivo
					count += 1
					#file_output.write("\n" + nombre_archivo + "\n")


					pref = "flickr30k_images/"
					foto = Foto(nombre_archivo=pref + nombre_archivo)
					foto.save()


				#print descripcion
				#file_output.write(translation)
				#file_output.write("\n")

				descripcion = descripcion.strip()

				descripcion_foto = DescripcionFoto(foto=foto, descripcion=descripcion)
				descripcion_foto.save()

				ultimo_texto = nombre_archivo



				if limit == 0:
					break
				#limit -= 1

	#file_output.close()



## ELIMINAMOS REGISTROS Y CARGAMOS BASE DE DATOS

# DescripcionFoto.objects.all().delete()
# Foto.objects.all().delete()
# cargar_bd()

# 	count = 0
# 	for descripcion in DescripcionFoto.objects.all():
# 		length_descripcion = len(descripcion.descripcion.split())
# 		count += length_descripcion
# 	
# 	
# 	print "Cantidad de palabras: ", count
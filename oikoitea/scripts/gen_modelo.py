# -*- coding: utf-8 -*-

import re
import sys

import urllib, json





"""
SI FALLA CARGAR DB POR PROBLEMA DE UTF-8

use oikoitea_development;
ALTER TABLE fotos_descripcionfoto MODIFY COLUMN descripcion LONGTEXT CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;

SET @@global.sql_mode= 'NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';


"""

def entrenar():
	filename = "/home/andres/Dropbox/oikoitea/scripts/traducciones/token-espanhol.txt"

	limit = 20
	count = 0

	ultimo_texto = ''


	#file_output = open("/home/andres/Dropbox/oikoitea/scripts/traducciones/text-formatted3.txt", "a") 

	#translator = Translator(to_lang="es")

	last = "1000092795.jpg"
	found = True


	foto = None

	lista_oraciones = []

	with open(filename) as f:
		for line in f:
			str_split = re.compile("^(\d+\.jpg)#(\d)\s+(.+)").split(line)

			nombre_archivo 	= str_split[1]
			numero_texto 	= str_split[2]
			descripcion		= str_split[3]
			
			if found:
				if ultimo_texto != nombre_archivo:
					#print "\n", nombre_archivo
					count += 1
					#file_output.write("\n" + nombre_archivo + "\n")

				#print descripcion
				#file_output.write(translation)
				#file_output.write("\n")

				descripcion = descripcion.strip()
				lista_oraciones.append( descripcion.split() )

				ultimo_texto = nombre_archivo



				if limit == 0:
					break
				#limit -= 1

	#file_output.close()

	


entrenar()
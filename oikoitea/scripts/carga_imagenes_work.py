# -*- coding: utf-8 -*-

import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import urllib, json



def get_translation(descripcion):
	translation = ""

	try:
		params = { "source": "en", "target": "es", "q": descripcion }
		url_params = urllib.urlencode(params)
		url = "  https://statickidz.com/scripts/traductor/?" + url_params
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		translation = data["translation"]
	except IOError as e:
		return get_translation(descripcion)

	return translation


def formatear_archivo_2():
	filename = "/home/andres/Dropbox/oikoitea/scripts/traducciones/parte7.txt"

	limit = 20
	count = 0

	ultimo_texto = ''


	file_output = open("/home/andres/Dropbox/oikoitea/scripts/traducciones/text-formatted3.txt", "a") 

	#translator = Translator(to_lang="es")

	last = "39999879.jpg"
	found = False

	with open(filename) as f:
		for line in f:
			str_split = re.compile("^(\d+\.jpg)#(\d)\s+(.+)").split(line)

			nombre_archivo 	= str_split[1]
			numero_texto 	= str_split[2]
			descripcion		= str_split[3]

			if last == nombre_archivo:
				found = True
				print "Encontrado"
			
			if found:
				if ultimo_texto != nombre_archivo:
					print "\n", nombre_archivo
					count += 1
					file_output.write("\n" + nombre_archivo + "\n")


				translation = get_translation(descripcion)
				file_output.write(translation)
				file_output.write("\n")

				ultimo_texto = nombre_archivo



				if limit == 0:
					break
				#limit -= 1

	file_output.close()



# formatear_archivo_2()
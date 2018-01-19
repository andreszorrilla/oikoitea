import sys

path 	= "/home/andres/Descargas/dataset_spanish/clean_corpus/spanish_billion_words/spanish_billion_words_"

for i in xrange(0,99):
	str_num = '%02d' % i
	filename = path + str_num
	with open(filename) as f:		
		for line in f:
			line = line.strip()
			if line == '': 	continue
			print filename


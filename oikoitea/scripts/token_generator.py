import sys
path = "/home/andres/Dropbox/oikoitea/scripts/traducciones/"


file_output = open("/home/andres/Dropbox/oikoitea/scripts/traducciones/token-espanhol.txt", "a") 

for i in xrange(1,9):
	filename = path + "text-formatted"  + str(i) + ".txt"
	with open(filename) as f:
		count = 6
		k = 0
		image_name = ""
		for line in f:
			line = line.strip()
			if line == '': 	continue
			
			if count == 6:
				image_name = line
			else:
				linea = image_name + "#" + str(5 - count) + "\t" + line
				file_output.write(linea)
				file_output.write("\n")


			count -= 1

			if count == 0:
				count = 6
				
			# 	if k == 1000:
			# 		sys.exit(0)
			k += 1



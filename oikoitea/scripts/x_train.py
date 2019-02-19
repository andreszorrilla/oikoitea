# import modules & set up logging
import gensim, logging
import os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)





class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()

#sentences = MySentences('/home/andres/Documents/tesis/modelos_esp/clean_corpus/1') # a memory-friendly iterator
#model = gensim.models.Word2Vec(sentences, sg=1, workers=4, size=300, window=10, negative=20, hs=1)
#model.save("prueba.bin")

sentences = [
				['perro', 'come', 'comida'],
				['gato', 'come', 'comida'],
				['gato', 'bebe', 'bebida'],
				['comida', 'es', 'rica']
			]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1, workers=4, sg=1, window=10, negative=20, hs=1)
model.save("prueba.bin")


print( model.most_similar("comida") )
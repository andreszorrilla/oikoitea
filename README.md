# Oikoitea


This Project is my Final Degree Work that consists in an Application based on Image 
Retrieval by text using tecniques of *Natural Language Processing* applied to the management of a Visual Agenda for Specialists that interact with people with Autism Spectrum Disorder.

People with ASD present mainly problems with social interaction, problems with language expression, communication and thinking.

To achieve communication with people with ASD, Augmentative and Alternative Systems are used, which are forms of expression other than verbal language, which includes various systems of symbols, both graphics (photographs, drawings, pictograms, words or letters) and gestures (mimicry) , gestures or manual signs).

There are applications that allow the dynamic management of visual agendas, but these applications allow you to search the images manually from the device, or by means of predefined text labels that are associated with the image.

There is a limitation when looking for images because the image does not have a correct description, obtaining unexpected results or with less precision than what is desired.

The application consists of a visual agenda based on the description images contents using Natural Language Processing (NLP), instead of the typical search which consists in the comparison of image text labels with the search term entered, therefore looking for precision in the results of the search.



Development environment
---------
* **Programming Language:** Python 2.7.5
* **Development Framework:** Django 1.8
* **Front End:**
	* HTML5
	* CSS3
	* Jquery.

* **Database:** MySQL 14.14
* **Libraries for Natural Language Processing (PLN) and Word Embeddings:**
	* **Gensim:** set of Python libraries that contain Word2vec implementations used for Word Embeddings.
	* **Annoy:** is responsible for searching for points in space that are close to a given reference point. It contains implementations of Euclidean Distance, Manhatan, Cosine and Hamming.


Images
---------
First to all, we need to get images with captions to make the search algoritm. So, we get a lot of images with detailed descriptions from diferents sources:
* [30k images with descriptions](http://shannon.cs.illinois.edu/DenotationGraph/): To produce the denotation graph, there were created an image caption corpus consisting of 158,915 crowd-sourced captions describing 31,783 images.
**Reference:** Bryan A. Plummer, Liwei Wang, Christopher M. Cervantes, Juan C. Caicedo, Julia Hockenmaier, and Svetlana Lazebnik, Flickr30k Entities: Collecting Region-to-Phrase Correspondences for Richer Image-to-Sentence Models, IJCV, 123(1):74-93, 2017.

* [Pictograms from Arasaac](http://www.arasaac.org/index.php): This website provides a lot a images with short descriptors, used in resources for no verbal communication, thought Alternative and Augmentative Communication Systems.


Word Corpus
---------
This applications is being built in spanish, so, we need a need a resource with a lot of words.
* [Spanish Billion Word Corpus and Embeddings](http://crscardellino.me/SBWCE/): This resource consists of an unannotated corpus of the Spanish language of nearly 1.5 billion words, compiled from different corpora and resources from the web; and a set of word vectors (or embeddings), created from this corpus using the word2vec algorithm, provided by the gensim package. These embeddings were evaluated by translating to Spanish word2vec’s word relation test set.


Search
---------

__author__ = 'Danny'

from gensim.models import Word2Vec

m = Word2Vec.load('mh370')
print m.similarity('Fariq', 'Zaharie')
print m.similarity('Fariq', 'Najib')
print m.similarity('Minh', 'Najib')
print m.similarity('Minh', 'Pham')
# print m.most_similar('Zaharie')
# model.most_similar('Najib', 5)

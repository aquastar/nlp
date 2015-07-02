__author__ = 'Danny'

from gensim.models import Word2Vec
import os.path
import pickle
import numpy as np
import scipy.stats as stats
import pylab as pl
import matplotlib.pyplot as plt
import os.path

model = Word2Vec.load('mh370_word2vec')
# print model.similarity('Fariq', 'Zaharie')
# print model.similarity('Fariq', 'Najib')
# print model.similarity('Tony', 'Najib')
# print model.similarity('Minh', 'Pham')

# print m.most_similar('Zaharie')
# model.most_similar('Najib', 5)

sim_list = []
entity_pair_sim_dict = {}

isExist = os.path.isfile('word2vec_entity_sim.pkl')
isExist = isExist and os.path.isfile('word2vec_entity_pair_sim.pkl')

if isExist:
    sim_list = pickle.load(open('word2vec_entity_sim.pkl'))
    entity_pair_sim_dict = pickle.load(open('word2vec_entity_pair_sim.pkl'))
else:
    topic = open('entity_name')
    entity_list = []

    while 1:
        lines = topic.readlines(100000)
        if not lines:
            break

        for line in lines:
            entity_list.append(line.strip())

    for i in range(0, len(entity_list)):
        inner_dict = {}
        for j in range(0, len(entity_list)):
            # print i, "-", j
            # print entity_list[i], "-", entity_list[j]
            try:
                sim = model.similarity(entity_list[i].capitalize(), entity_list[j].capitalize())
                sim_list.append(sim)
                inner_dict[entity_list[j].lower()] = sim
            except:
                print "Caught it!,", entity_list[i], "-", entity_list[j], "-", i, "-", j
        entity_pair_sim_dict[entity_list[i].lower()] = inner_dict
    f_word2vec_entity_sim = open('word2vec_entity_sim.pkl', 'wb')
    f_word2vec_entity_pair_sim = open('word2vec_entity_pair_sim.pkl', 'wb')
    pickle.dump(sim_list, f_word2vec_entity_sim)
    pickle.dump(entity_pair_sim_dict, f_word2vec_entity_pair_sim)

sim_list.sort()
hmean = np.mean(sim_list)
hstd = np.std(sim_list)

fit = stats.norm.pdf(sim_list, hmean, hstd)
pl.plot(sim_list, fit, '-o')
pl.hist(sim_list, normed=True)
pl.show()

pdf = stats.norm.pdf(sim_list, hmean, hstd)
plt.plot(sim_list, pdf)

# print 'here we go'
print entity_pair_sim_dict['najib']['tony']
print entity_pair_sim_dict['najib']['anwar']
print entity_pair_sim_dict['najib']['minh']

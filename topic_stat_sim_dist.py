from math import log
import pickle
import numpy as np
import scipy.stats as stats
import pylab as pl
import matplotlib.pyplot as plt
import os.path


class JSD:
    def KLD(self, p, q):
        if 0 in q:
            raise ValueError
        return sum(_p * log(_p / _q) for (_p, _q) in zip(p, q) if _p != 0)

    def JSD_core(self, p, q):
        M = [0.5 * (_p + _q) for _p, _q in zip(p, q)]
        return 0.5 * self.KLD(p, M) + 0.5 * self.KLD(q, M)


jsd = JSD()
# print jsd.JSD_core([1,2,3],[0,0.000001,0]) #2.07943413392
# exit(0)

def getSimBetween(e1, e2):
    e1list = []
    e2list = []

    if e1 not in word_dist_dict or e2 not in word_dist_dict:
        return 1

    for t in range(0, 29):
        if str(t) in word_dist_dict[e1] and word_dist_dict[e1][str(t)] > 0.0:
            e1list.append(float(word_dist_dict[e1][str(t)]))
        else:
            e1list.append(0.0000001)

        if str(t) in word_dist_dict[e2] and word_dist_dict[e2][str(t)] > 0.0:
            e2list.append(float(word_dist_dict[e2][str(t)]))
        else:
            e2list.append(0.0000001)

    return jsd.JSD_core(e1list, e2list)


word_dist_dict = pickle.load(open('word_dist_dict.pkl'))

isExist = os.path.isfile('topic_entity_sim.pkl')
isExist = isExist and os.path.isfile('topic_entity_pair_sim.pkl')
sim_list = []
entity_pair_sim_dict = {}
if isExist:
    sim_list = pickle.load(open('topic_entity_sim.pkl'))
    entity_pair_sim_dict = pickle.load(open('topic_entity_pair_sim.pkl'))
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
            print i, "-", j
            # print entity_list[i], "-", entity_list[j]
            sim = getSimBetween(entity_list[i].lower(), entity_list[j].lower())
            sim_list.append(sim)
            inner_dict[entity_list[j].lower()] = sim
        entity_pair_sim_dict[entity_list[i].lower()] = inner_dict
    f_topic_entity_pair_sim = open('topic_entity_pair_sim.pkl', 'wb')
    f_topic_entity_sim = open('topic_entity_sim.pkl', 'wb')
    pickle.dump(entity_pair_sim_dict, f_topic_entity_pair_sim)
    pickle.dump(sim_list, f_topic_entity_sim)

sim_list.sort()
hmean = np.mean(sim_list)
hstd = np.std(sim_list)

fit = stats.norm.pdf(sim_list, hmean, hstd)
pl.plot(sim_list, fit, '-o')
pl.hist(sim_list, normed=True)
pl.show()



# print 'here we go'
print getSimBetween('najib', 'tony')
print getSimBetween('najib', 'mansor')
print getSimBetween('najib', 'rosmah')
# print word_dist_dict['najib']
# print word_dist_dict['mansor']

# print entity_pair_sim_dict['najib']['mansor']

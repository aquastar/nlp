from math import log
import pickle

class JSD:
    def KLD(self, p, q):
        if 0 in q:
            raise ValueError
        return sum(_p * log(_p / _q) for (_p, _q) in zip(p, q) if _p != 0)

    def JSD_core(self, p, q):
        M = [0.5 * (_p + _q) for _p, _q in zip(p, q)]
        return 0.5 * self.KLD(p, M) + 0.5 * self.KLD(q, M)

# ********Test*******
p = [.25, 0.9, .2]
q = [.25, 0.9, 0.31]

jsd = JSD()
# print jsd.KLD(p,q)
print jsd.JSD_core(p, q)
# print jsd.JSD_core(q,p)

e1 = 'najib'
e2 = 'tony'
e1list = []
e2list = []

word_dist_dict = pickle.load(open('word_dist_dict.pkl'))
for i in range(0, 29):
    if str(i) in word_dist_dict[e1]:
        e1list.append(word_dist_dict[e1][str(i)])
    else:
        e1list.append(0)

    if str(i) in word_dist_dict[e2]:
        e2list.append(word_dist_dict[e2][str(i)])
    else:
        e2list.append(0)

print jsd.JSD_core(e1list, e2list)
print 1234
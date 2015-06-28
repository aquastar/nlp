from math import log


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

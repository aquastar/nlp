__author__ = 'Danny'

from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis

# brown_ic = wordnet_ic.ic('ic-brown.dat')
# semcor_ic = wordnet_ic.ic('ic-semcor.dat')
genesis_ic = wn.ic(genesis, False, 0.0)

phd = wn.synset('ph.d..n.01')
prof = wn.synset('professor.n.01')
res = wn.synset('research.n.01')

print phd.path_similarity(res)
print phd.lch_similarity(res)
print phd.wup_similarity(res)

print prof.path_similarity(res)
print prof.lch_similarity(res)
print prof.wup_similarity(res)

# Wu-Palmer Similarity: Return a score denoting how similar two word senses are,
# based on the depth of the two senses in the taxonomy and that of their Least Common Subsumer
# (most specific ancestor node). Note that at this time the scores given do _not_ always agree
# with those given by Pedersen's Perl implementation of Wordnet Similarity.

# print dog.res_similarity(cat, brown_ic)
# print dog.res_similarity(cat, genesis_ic)

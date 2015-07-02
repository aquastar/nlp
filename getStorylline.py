__author__ = 'Danny'

import pickle

# load sim matrix
topic_entity_sim_dict = pickle.load(open('topic_entity_pair_sim.pkl'))
word2vec_entity_sim_dict = pickle.load(open('word2vec_entity_pair_sim.pkl'))


def isTopicStrong(e1, e2):
    if e1 in topic_entity_sim_dict and e2 in topic_entity_sim_dict[e1]:
        return topic_entity_sim_dict[e1][e2] < 0.005
    else:
        return False


def isWord2vecStrong(e1, e2):
    if e1 in word2vec_entity_sim_dict and e2 in word2vec_entity_sim_dict[e1]:
        return word2vec_entity_sim_dict[e1][e2] > 0.6
    else:
        return False


# search algorithm
def getStoryline(e1, e2, max):
    storylines = [[e1]]

    some_less_than_max = True
    while some_less_than_max:
        for k in storylines:
            if len(k) >= max:
                some_less_than_max = False
                continue
            print "[k]: ", k
            some_less_than_max = True

            last_entity = k[-1]
            if last_entity == e2:
                continue
            for kk in topic_entity_sim_dict[last_entity]:
                # print len(topic_entity_sim_dict[last_entity])

                if kk == e1:
                    continue

                if isTopicStrong(last_entity, kk) or isWord2vecStrong(last_entity, kk):
                    storylines.append(k + [kk])
                    # print "add kk"
                print  len(storylines)
                # raw_input()
            if e2 not in k:
                storylines.remove(k)
                # print "remove k"

    return storylines


e1 = 'ali'
e2 = 'pouria'
max = 6
print getStoryline(e1, e2, max)


# rank some triples for explanation

import gensim
import logging

NUM_TOPICS = 30

logging.basicConfig(format='%(message)s',
                    level=logging.INFO, filename='topicInfo')
lda = gensim.models.LdaModel.load('mh370_topic')

lda.print_topics(NUM_TOPICS, num_words=500)

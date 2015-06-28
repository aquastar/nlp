import gensim
import logging

NUM_TOPICS = 15

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

lda = gensim.models.LdaModel.load('mh370')
lda.print_topics(NUM_TOPICS, num_words=500)

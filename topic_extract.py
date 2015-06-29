import logging
import os
import nltk
import gensim


def iter_docs(topdir, stoplist):
    for fn in os.listdir(topdir):
        fin = open(os.path.join(topdir, fn), 'rb')
        text = fin.read()
        fin.close()
        yield (x for x in
               gensim.utils.tokenize(text, lowercase=True, deacc=True,
                                     errors="ignore")
               if x not in stoplist)


class MyCorpus(object):
    def __init__(self, topdir, stoplist):
        self.topdir = topdir
        self.stoplist = stoplist
        self.dictionary = gensim.corpora.Dictionary(iter_docs(topdir, stoplist))

    def __iter__(self):
        for tokens in iter_docs(self.topdir, self.stoplist):
            yield self.dictionary.doc2bow(tokens)


NUM_TOPICS = 30
TEXTS_DIR = "text"
MODELS_DIR = "."

stoplist = set(nltk.corpus.stopwords.words("english"))
corpus = MyCorpus(TEXTS_DIR, stoplist)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)
# for saving, rbl
corpus.dictionary.save(os.path.join(MODELS_DIR, "mtsamples.dict"))
gensim.corpora.MmCorpus.serialize(os.path.join(MODELS_DIR, "mtsamples.mm"), corpus)
dictionary = gensim.corpora.Dictionary.load(os.path.join(MODELS_DIR, "mtsamples.dict"))
corpus = gensim.corpora.MmCorpus(os.path.join(MODELS_DIR, "mtsamples.mm"))

lda = gensim.models.LdaModel(corpus, id2word=dictionary, num_topics=NUM_TOPICS, update_every=1, chunksize=500, passes=20)
lda.save('mh370')
# lda.print_topics(NUM_TOPICS, num_words=500)
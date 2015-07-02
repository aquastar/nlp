from gensim.models import Word2Vec
import nltk
import string
import os

base = 'text'
str = []
wordMatrix = []
temp = []
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk(base):
    path = root.split('/')

    for file in files:

        ff = open(path[0] + '\\' + file)
        lines = ff.readlines()
        if not lines:
            continue

        for line in lines:
            sents = tokenizer.tokenize(line.decode("utf-8"))

            for sent in sents:
                tempsent = ' '.join(word.strip(string.punctuation) for word in sent.split()).encode("utf-8")
                # print tempsent
                temp.append(tempsent)
                tokens = nltk.word_tokenize(tempsent)

                wordMatrix.append(tokens)
                for token in tokens:
                    if token not in str:
                        str.append(token)

for index in range(len(str)):
    strsplit = str[index].strip(string.punctuation)

# just save
b = Word2Vec(wordMatrix)
b.save('mh370_word2vec')

exit(0)

# print every entity pair
strlen = len(strsplit)
for index in range(strlen):
    if strsplit[index][0:1].isupper():
        print b.most_similar(strsplit[index], topn=strlen - 1)

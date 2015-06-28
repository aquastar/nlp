from nltk.tag.stanford import NERTagger
import os

java_path = "C:/Program Files/Java/jdk1.8.0_45/bin/java.exe"
os.environ['JAVAHOME'] = java_path

st = NERTagger('./english.all.7class.distsim.crf.ser.gz', './stanford-corenlp-3.5.2.jar')

file = open("text/289007975")

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        print st.tag(unicode(line, errors='ignore').split())

import sys, codecs
import nltk.data
from nltk.tokenize import RegexpTokenizer

'''synarthsh pou dhmiourgei lista me to katharo keimeno ana ethnikothta'''
def freq_words_nationality(l, write, write_open):

    #write = codecs.open("text", "wb", "utf-8")
    #write_open = codecs.open("text", "rb", "utf-8")
    for q in l:
        write.write(q)
    stopwords = set(nltk.corpus.stopwords.words('english'))
    temp = write_open.read().replace('\n', ' ')
    temp1 = RegexpTokenizer(r'\w+').tokenize(temp)
    allWordExceptStopDist = nltk.FreqDist(w.lower() for w in temp1 if w not in stopwords)

    return allWordExceptStopDist

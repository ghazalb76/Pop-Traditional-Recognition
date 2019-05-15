import nltk
from nltk.collocations import *
from nltk import ngrams
import glob

class Pop_manager():
    def __init__(self):
        self.read_files()

    pop_text = ''
    def read_files(self):
        for pop_lyric_file in glob.glob("../../SplitData/train/pop/*.txt"):

            txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
            for line in txt_file.readlines():
                    self.pop_text += line
        print(self.pop_text)

def ngram_words(text, n):

    n_gram = ngrams(sentence.split(), n)
    fdist = nltk.FreqDist(n_gram)
    n_gram = []
    for t,v in fdist:
        n_gram.append(t+' '+v)
    return n_gram

pop_manager = Pop_manager()
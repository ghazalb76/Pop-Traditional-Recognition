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


def ngram_words(text, n):
    n_gram = ngrams(text.split(), n)
    fdist = nltk.FreqDist(n_gram)
    n_gram = []
    for t in fdist:
        if n == 1:
            n_gram.append(t[0])
        elif n == 2:
            n_gram.append(t[0]+' '+t[1])
        elif n == 3:
            n_gram.append(t[0]+' '+t[1]+' '+t[2])
    return n_gram

pop_manager = Pop_manager()
one_gram_list = ngram_words(pop_manager.pop_text, 1)
two_gram_list = ngram_words(pop_manager.pop_text, 2)
three_gram_list = ngram_words(pop_manager.pop_text, 3)
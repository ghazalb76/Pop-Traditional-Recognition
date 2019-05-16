import nltk
from nltk.collocations import *
from nltk import ngrams
import glob
from collections import Counter

class Ngram_manager():
    ngram_list = []
    def ngram_words(self, text, n):
        n_gram = ngrams(text.split(), n)
        fdist = nltk.FreqDist(n_gram)
        for t in fdist:
            if n == 1:
                self.ngram_list.append(t[0])
            elif n == 2:
                self.ngram_list.append(t[0]+' '+t[1])
            elif n == 3:
                self.ngram_list.append(t[0]+' '+t[1]+' '+t[2])
        return self.ngram_list

    def calculate_probability(self, thisWord, wholeWord, types):
        return (thisWord+1)/(wholeWord+types+1)


class Pop_manager():
    pop_text = ''
    pop_dict = {}
    pop_words = []
    ngram_manager = Ngram_manager()
    def __init__(self):
        self.read_files()
        self.make_dict()
        print(len(self.pop_dict))

    def read_files(self):
        for pop_lyric_file in glob.glob("../../SplitData/train/pop/*.txt"):

            txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
            for line in txt_file.readlines():
                    self.pop_text += line

        self.pop_words = self.pop_text.split(' ')

    def make_dict(self):
        for word in self.pop_words:
            if word in self.pop_dict:
                self.pop_dict[word] += 1
            else:
                self.pop_dict[word] = 1
    
    def ngram_handler(self):
        unigram_list = self.ngram_manager.ngram_words(self.pop_text, 1)
        wholeWords = 0
        unigram_counts = []
        for word in self.pop_dict:
            wholeWords += self.pop_dict[word]

        for unigram in unigram_list:
            unigram_counts.append((self.ngram_manager.calculate_probability(self.pop_dict[unigram], wholeWords, len(self.pop_dict)))*1000)
        print(unigram_counts)
        # two_gram_list = self.ngram_manager.ngram_words(self.pop_text, 2)
        # three_gram_list = self.ngram_manager.ngram_words(self.pop_text, 3)
        # unigram = self.ngram_manager.calculate_onegram(unigram_list)

    # def pop_types(self):





pop_manager = Pop_manager()
pop_manager.ngram_handler()
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
        if n == 1:
            self.ngram_list = []
            for t in fdist:
                self.ngram_list.append(t[0])
        elif n == 2:
            self.ngram_list = []
            for t in fdist:
                self.ngram_list.append(t[0]+' '+t[1])
        elif n == 3:
            self.ngram_list = []
            for t in fdist:
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

    def read_files(self):
        # ../../SplitData/train/pop/*.txt
        for pop_lyric_file in glob.glob("test/in.2gram"):

            txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
            for line in txt_file.readlines():
                line = line.rstrip()
                line += ' '
                self.pop_text += line

        self.pop_words = self.pop_text.split(' ')
        for word in self.pop_words:
            if word is '':
                self.pop_words.remove('')

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
            unigram_counts.append((self.ngram_manager.calculate_probability(self.pop_dict[unigram], wholeWords, len(self.pop_dict))))
        print("************* unigram ************")
        for i in range(0,len(unigram_list)):
            print(unigram_list[i], "|", unigram_counts[i])
        print("\n\n")
 
        print("************* biagram ************")
        two_gram_list = self.ngram_manager.ngram_words(self.pop_text, 2)
        for word in two_gram_list:
            counter = 0
            words = word.split(' ')
            for i in range(0, len(self.pop_words)-1):
                if self.pop_words[i] == words[0] and self.pop_words[i+1] == words[1]:
                    counter +=1
            biagram_counts = self.ngram_manager.calculate_probability(counter, self.pop_dict[words[0]], len(self.pop_dict))
            print(words[0], "|", words[1], "|", biagram_counts)
        print("\n\n")



        # three_gram_list = self.ngram_manager.ngram_words(self.pop_text, 3)

    # def pop_types(self):





pop_manager = Pop_manager()
pop_manager.ngram_handler()
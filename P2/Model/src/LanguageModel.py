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


    def unigram(self, text, dictionary):
        print("************* unigram ************")
        unigram_list = self.ngram_words(text, 1)
        unigram_list.remove('<s>')
        unigram_list.remove('</s>')
        wholeWords = 0
        unigram_counts = []
        for word in dictionary:
            if word != '<s>' and word != '</s>':
                wholeWords += dictionary[word]
        for unigram in unigram_list:
            unigram_counts.append((self.calculate_probability(dictionary[unigram], wholeWords, len(dictionary)-2)))
        for i in range(0,len(unigram_list)):
            print(unigram_list[i], "|", unigram_counts[i])
        print("\n\n")


    def biagram(self, text, dictionary, label_words):
        print("************* biagram ************")
        biagram_list = self.ngram_words(text, 2)
        biagram_list_distinct = []
        for word in biagram_list:
            if word not in biagram_list_distinct:
                biagram_list_distinct.append(word)

        for word in biagram_list_distinct:
            counter = 0
            words = word.split(' ')
            if words[0] != '</s>':
                for i in range(0, len(label_words)-1):
                    if label_words[i] == words[0] and label_words[i+1] == words[1]:
                        counter +=1
                biagram_counts = self.calculate_probability(counter, dictionary[words[0]], len(dictionary)-2)
                print(words[0], "|", words[1], "|", biagram_counts)
        print("\n\n")


    def triagram(self, text, dictionary, label_words):
        print("************* trigram ************")
        trigram_list = self.ngram_words(text, 3)
        trigram_list_distinct = []
        for word in trigram_list:
            if word not in trigram_list_distinct:
                trigram_list_distinct.append(word)

        for word in trigram_list_distinct:
            two_counter = 0
            three_counter = 0
            words = word.split(' ')
            if words[0] != '</s>' and words[1] != '</s>':
                for i in range(0, len(label_words)-2):
                    if label_words[i] == words[0] and label_words[i+1] == words[1]:
                        two_counter += 1
                        if label_words[i+2] == words[2]:
                            three_counter += 1
                trigram_counts = self.calculate_probability(three_counter, two_counter, len(dictionary)-2)
                print(words[0], "|", words[1], "|", words[2], "|", trigram_counts)
        print("\n\n")
        


class Pop_manager():
    pop_text = '<s> '
    pop_dict = {}
    pop_words = []
    ngram_manager = Ngram_manager()
    def __init__(self):
        self.read_files()
        self.make_dict()

    def read_files(self):
        # ../../SplitData/train/pop/*.txt
        for pop_lyric_file in glob.glob("../test/in.2gram"):

            txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
            for line in txt_file.readlines():
                line = line.rstrip()
                line += ' </s> <s> '
                self.pop_text += line

        pop_wordss = self.pop_text.split(' ')
        for i in range(0,len(pop_wordss)-2):
            self.pop_words.append(pop_wordss[i])
        for word in self.pop_words:
            if word is '':
                self.pop_words.remove('')
        # print(self.pop_words)

    def make_dict(self):
        for word in self.pop_words:
                if word in self.pop_dict:
                    self.pop_dict[word] += 1
                else:
                    self.pop_dict[word] = 1
    
    def ngram_handler(self):
        self.ngram_manager.unigram(self.pop_text, self.pop_dict)
        self.ngram_manager.biagram(self.pop_text, self.pop_dict, self.pop_words)
        self.ngram_manager.triagram(self.pop_text, self.pop_dict, self.pop_words)



pop_manager = Pop_manager()
pop_manager.ngram_handler()
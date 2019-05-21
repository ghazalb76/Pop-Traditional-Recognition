import glob
import math


def read_ngrams(i):
        gram_text = open("../../Model/test/ref."+str(i)+"gram.lm", 'r', encoding="utf-8")
        gram = []
        for line in gram_text.readlines():
                line.rstrip("\n")
                gram.append(line.split('|'))
        for word in gram:
                word[i] = float(word[i])
        return gram


def read_text():
        pop_text = '<s> '
        pop_words = []
        for pop_lyric_file in glob.glob("../../Model/test/in.1gram"):
                txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        line = line.rstrip()
                        line += ' </s> <s> '
                        pop_text += line
        pop_wordss =  pop_text.split(' ')
        for i in range(0, len(pop_wordss)-2):
                pop_words.append(pop_wordss[i])
        return pop_words

def change_uni_UNK(unigram):
        words_ = []
        pop_words_UNK = []
        for i in range(0, len(unigram)):
                words_.append(unigram[i][0])
        for word in pop_words:
                if word in words_:
                        pop_words_UNK.append(word)
                elif word != '<s>' and word != '</s>':
                        pop_words_UNK.append("UNK")
        return pop_words_UNK

def change_ngram_UNK(unigram):
        words_ = []
        pop_words_UNK = []
        for i in range(0, len(unigram)):
                words_.append(unigram[i][0])
        for word in pop_words:
                if word in words_ or word == '<s>' or word == '</s>':
                        pop_words_UNK.append(word)
                else:
                        pop_words_UNK.append("UNK")

        return pop_words_UNK


def uni_perplexity(pop_words, unigram):
        unigram_perplexity = 1
        for word in pop_words:
                for per in unigram:
                        if word == per[0]:
                                unigram_perplexity *= 1/per[1]
                                # print(per[0], "|", 1/per[1])

        temp = str(unigram_perplexity)
        unigram_perplexity = float(temp[0:6])
        unigram_perplexity = math.pow(unigram_perplexity, len(pop_words))
        print("unigram perplexity: ", unigram_perplexity)


def bia_perplexity(pop_words_distinct, biagram):
        biagram_perplexity = 1
        for i in range(0, len(pop_words_distinct)-1):
                for per in biagram:
                        if pop_words_distinct[i] == per[0] and pop_words_distinct[i+1] == per[1]:
                                # print(per[0], "|", per[1], "|", per[2])
                                biagram_perplexity *= 1/per[2]

        temp = str(biagram_perplexity)
        biagram_perplexity = float(temp[0:6])
        biagram_perplexity = math.pow(biagram_perplexity, len(pop_words_distinct))
        print("bigram perplexity: ",biagram_perplexity)


def tri_perplexity(pop_words_distinct, biagram):
        triagram_perplexity = 1
        for i in range(0, len(pop_words_distinct)-2):
                for per in triagram:
                        if pop_words_distinct[i] == per[0] and pop_words_distinct[i+1] == per[1] and pop_words_distinct[i+2] == per[2]:
                                # print(per[0], "|", per[1], "|", per[2], "|", per[3])
                                triagram_perplexity *= 1/per[3]

        temp = str(triagram_perplexity)
        triagram_perplexity = float(temp[0:6])
        triagram_perplexity = math.pow(triagram_perplexity, len(pop_words_distinct))
        print("trigram perplexity: ",triagram_perplexity)



pop_words = read_text()
unigram = read_ngrams(1)
biagram = read_ngrams(2)
triagram = read_ngrams(3)
pop_words_UNK = change_uni_UNK(unigram)
uni_perplexity(pop_words_UNK, unigram)
pop_words_UNK = change_ngram_UNK(biagram)
bia_perplexity(pop_words_UNK, biagram)
tri_perplexity(pop_words_UNK, triagram)


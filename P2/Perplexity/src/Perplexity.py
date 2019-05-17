import glob
import math


def read_biagram(i):
        gram_text = open("../../Model/test/out."+str(i)+"gram.lm", 'r', encoding="utf-8")
        gram = []
        for line in gram_text.readlines():
                line.rstrip("\n")
                gram.append(line.split('|'))
        for word in gram:
                word[i] = float(word[i])
        return  gram


def read_text():
        pop_text = '<s> '
        pop_words = []
        for pop_lyric_file in glob.glob("../../Model/test/in.1gram"):
                txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        line = line.rstrip()
                        line += ' </s> <s> '
                        pop_text += line
        txt_file = open("oo.txt", 'w', encoding="utf-8")
        txt_file.write( pop_text)
        pop_wordss =  pop_text.split(' ')
        for i in range(0, len(pop_wordss)-2):
                pop_words.append(pop_wordss[i])

        pop_words_distinct = []
        for word in pop_words:
                if word != '<s>' and word != '</s>' and word not in pop_words_distinct and word is not '':
                        pop_words_distinct.append(word)
        return pop_words_distinct



pop_words_distinct = read_text()
unigram = read_biagram(1)
print(unigram)
biagram = read_biagram(2)
print(biagram)
biagram = read_biagram(3)
print(biagram)
# -*- coding: utf-8 -*-
from hazm import *
import glob


normalizer = Normalizer()

def pop_processing():
        all_texts = open("../pop/pop.txt", 'w', encoding="utf-8")
        pop_text = ''

        for pop_lyric_file in glob.glob("../../Data/pop/*.txt"):
                txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        pop_text += line

        pop_text = normalizer.normalize(pop_text)
        pop_text = word_tokenize(pop_text)

        for word in pop_text:
                word += ' '
                all_texts.write(word)



def traditional_processing():
        all_texts = open("../traditional/traditional.txt", 'w', encoding="utf-8")
        traditional_text = ''

        for traditional_lyric_file in glob.glob("../../Data/traditional/*.txt"):
                txt_file = open(traditional_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        traditional_text += line

        traditional_text = normalizer.normalize(traditional_text)
        traditional_text = word_tokenize(traditional_text)

        for word in traditional_text:
                word += ' '
                all_texts.write(word)


pop_processing()
traditional_processing()

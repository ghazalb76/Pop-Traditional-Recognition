# -*- coding: utf-8 -*-
from hazm import *
import glob
import io


normalizer = Normalizer()
unImportant_list = []
unImportant = open("unimportant.txt", 'r', encoding="utf-8")

for line in unImportant.readlines():
        unImportant_list.append(line)

def pop_processing():
        all_texts = open("out_pop_lyrics.txt", 'w', encoding="utf-8")
        pop_text = ''

        for pop_lyric_file in glob.glob("../RawData/train/pop/*.txt"):
                txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        pop_text += line

        pop_text = normalizer.normalize(pop_text)
        pop_text = word_tokenize(pop_text)

        pop_txt = []
        for word in pop_text:
                if word not in unImportant_list:
                        pop_txt.append(word)


        for word in pop_txt:
                word += ' '
                all_texts.write(word)




def traditional_processing():
        all_texts = open("out_traditional_lyrics.txt", 'w', encoding="utf-8")
        traditional_text = ''
        for traditional_lyric_file in glob.glob("../RawData/train/traditional/*.txt"):
                txt_file = open(traditional_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        traditional_text += line
        traditional_text = normalizer.normalize(traditional_text)
        traditional_text = word_tokenize(traditional_text)

        traditional_txt = []
        for word in traditional_text:
                if word not in unImportant_list:
                        traditional_txt.append(word)


        for word in traditional_txt:
                word += ' '
                all_texts.write(word)


pop_processing()
traditional_processing()
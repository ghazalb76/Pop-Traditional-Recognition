# -*- coding: utf-8 -*-
from hazm import *
import glob


normalizer = Normalizer()

def pop_processing():
        file_name_counter = 1
        for pop_lyric_file in glob.glob("../../Data/pop/*.txt"):
                pop_text = ''
                all_texts = open("../pop/"+str(file_name_counter)+".txt", 'w', encoding="utf-8")

                txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        print(line)
                        pop_text += line

                pop_text = normalizer.normalize(pop_text)
                pop_text = word_tokenize(pop_text)

                for word in pop_text:
                        word += ' '
                        all_texts.write(word)
                file_name_counter += 1



def traditional_processing():
        file_name_counter = 1
        for traditional_lyric_file in glob.glob("../../Data/traditional/*.txt"):
                traditional_text = ''
                all_texts = open("../traditional/"+str(file_name_counter)+".txt", 'w', encoding="utf-8")
                txt_file = open(traditional_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        traditional_text += line

                traditional_text = normalizer.normalize(traditional_text)
                traditional_text = word_tokenize(traditional_text)

                for word in traditional_text:
                        word += ' '
                        all_texts.write(word)
                file_name_counter += 1


pop_processing()
traditional_processing()

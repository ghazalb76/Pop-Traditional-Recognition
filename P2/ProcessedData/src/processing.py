# -*- coding: utf-8 -*-
from hazm import *
import glob


normalizer = Normalizer()

def pop_processing():
        file_name_counter = 1
        for pop_lyric_file in glob.glob("../../Data/pop/*.txt"):
                all_texts = open("../pop/"+str(file_name_counter)+".txt", 'w', encoding="utf-8")
                txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        pop_text = ''
                        line = normalizer.normalize(line)
                        line = word_tokenize(line)
                        for word in line:
                                pop_text += (word + ' ')
                        all_texts.write(pop_text + "\n")
                        
                file_name_counter += 1



def traditional_processing():
        file_name_counter = 1
        for traditional_lyric_file in glob.glob("../../Data/traditional/*.txt"):
                all_texts = open("../traditional/"+str(file_name_counter)+".txt", 'w', encoding="utf-8")
                txt_file = open(traditional_lyric_file, 'r', encoding="utf-8")
                for line in txt_file.readlines():
                        traditional_text = ''
                        line = normalizer.normalize(line)
                        line = word_tokenize(line)
                        for word in line:
                                traditional_text += (word + ' ')
                        all_texts.write(traditional_text + "\n")
                file_name_counter += 1


pop_processing()
traditional_processing()

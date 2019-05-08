# -*- coding: utf-8 -*-
from hazm import *
import glob
import io


normalizer = Normalizer()
unImportant_list = []
unImportant = open("unimportant.txt", 'r', encoding="utf-8")
for line in unImportant.readlines():
        unImportant_list.append(line)
print(unImportant_list)
all_texts = open("out_pop_lyrics.txt", 'w', encoding="utf-8")
pop_text = ''
for pop_lyric_file in glob.glob("../RawData/train/pop/*.txt"):
    txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
    for line in txt_file.readlines():
        pop_text += line
pop_text = normalizer.normalize(pop_text)
pop_text = word_tokenize(pop_text)

ttt = open("out_pop1_lyrics.txt", 'w', encoding="utf-8")
print("BEFORRRRRRRRRR:")
for item in pop_text:
        if item in unImportant_list:
               ttt.write(item)

print("AFTERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR:")




for unImp_word in unImportant_list:
        print(unImp_word)
        for word in pop_text:
                if word == unImp_word:
                        print("YES")

for word in pop_text:
        word += ' '
        all_texts.write(word)





all_texts = open("out_traditional_lyrics.txt", 'w', encoding="utf-8")
pop_text = ''
for pop_lyric_file in glob.glob("../RawData/train/traditional/*.txt"):
    txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
    for line in txt_file.readlines():
        pop_text += line
pop_text = normalizer.normalize(pop_text)
pop_text = word_tokenize(pop_text)

for unImp_word in unImportant_list:
        print(unImp_word)
        for word in pop_text:
                if word == unImp_word:
                        pop_text.remove(unImp_word)
for word in pop_text:
        word += ' '
        all_texts.write(word)
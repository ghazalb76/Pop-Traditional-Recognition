# -*- coding: utf-8 -*-

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display


def pop_freq():
    pop_text = open("../../ProcessedData/pop/pop.txt", 'r', encoding="utf-8")

    pop_word = []
    for line in pop_text.readlines():
        pop_word.append(line)

    pop_words = []
    for word in pop_word:
        pop_words = word.split(' ')

    pop_words_freq = {}
    for word in pop_words:
        if word in pop_words_freq:
            pop_words_freq[word] += 1
        else:
            pop_words_freq[word] = 1

    for word in pop_words_freq:
        pop_words_freq[word] /= (len(pop_words)/10000)

    return pop_words


def traditional_freq():
    traditional_text = open("../../ProcessedData/traditional/traditional.txt", 'r', encoding="utf-8")

    traditional_word = []
    for line in traditional_text.readlines():
        traditional_word.append(line)

    traditional_words = []
    for word in traditional_word:
        traditional_words = word.split(' ')

    traditional_words_freq = {}
    for word in traditional_words:
        if word in traditional_words_freq:
            traditional_words_freq[word] += 1
        else:
            traditional_words_freq[word] = 1

    for word in traditional_words_freq:
        traditional_words_freq[word] /= (len(traditional_words)/10000)

    return traditional_words


def diff_words(word_list1, word_list2):
    for word in word_list1:
        if word in word_list2:
            word_list1.remove(word)
            word_list2.remove(word)
    return word_list1


def prepare_cloud_text(words):
    cloud_text = ''
    for word in words:
        cloud_text += ' '
        cloud_text += word
    reshaped_text = reshape_text(cloud_text)
    generate_cloud(reshaped_text)


def reshape_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    reshaped_text = get_display(reshaped_text)
    return reshaped_text


def generate_cloud(my_wordCloud):
    print("Wait for creating wordcloud...")
    popWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
    popWordCloud.generate(my_wordCloud)
    plt.imshow(popWordCloud)
    plt.axis("off")

    plt.show()


pop_words = pop_freq()
traditional_words = traditional_freq()


pop_words_copy = pop_words
traditional_words_copy = traditional_words
pop_diff_traditional_words = diff_words(pop_words_copy, traditional_words_copy)
pop_words_copy = pop_words
traditional_words_copy = traditional_words
traditional_diff_pop_words = diff_words(traditional_words_copy, pop_words_copy)

''' pop without stopword '''
# prepare_cloud_text(pop_words)
''' traditional without stopword '''
# prepare_cloud_text(traditional_words)
''' pop diff traditional without stopwords'''
# prepare_cloud_text(pop_diff_traditional_words)
''' traditional diff pop without stopwords'''
# prepare_cloud_text(traditional_diff_pop_words)


#---------------------------- StopWords ----------------------#
stopword_list = []
unImportant = open("../stopwords.txt", 'r', encoding="utf-8")


for line in unImportant.readlines():
        stopword_list.append(line)
for sentence in stopword_list:
        stopword_list = sentence.split(' ')

#----------- pop ----------#
pop_words_freeStop = []
for word in pop_words:
        if word not in stopword_list:
                pop_words_freeStop.append(word)

#-------- traditonal -------#
traditional_words_freeStop = []
for word in traditional_words:
        if word not in stopword_list:
                traditional_words_freeStop.append(word)
#--------------------------------------------------------------#


pop_words_freeStop_copy = pop_words_freeStop
traditional_words_freeStop_copy = traditional_words_freeStop
pop_diff_traditional_words = diff_words(pop_words_freeStop_copy, traditional_words_freeStop_copy)
pop_words_freeStop_copy = pop_words_freeStop
traditional_words_freeStop_copy = traditional_words_freeStop
traditional_diff_pop_words = diff_words(traditional_words_freeStop_copy, pop_words_freeStop_copy)

''' pop without stopword '''
# prepare_cloud_text(pop_words_freeStop)
''' traditional without stopword '''
# prepare_cloud_text(traditional_words_freeStop)
''' pop diff traditional without stopwords'''
# prepare_cloud_text(pop_diff_traditional_words)
''' traditional diff pop without stopwords'''
# prepare_cloud_text(traditional_diff_pop_words)
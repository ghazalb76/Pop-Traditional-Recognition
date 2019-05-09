
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

def pop_freq():
    pop_text = open("../ProcessedData/out_pop_lyrics.txt", 'r', encoding="utf-8")

    pop_word = []
    for line in pop_text.readlines():
        print("Yes")
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
    # for word in pop_words_freq:
    #     print(pop_words_freq[word], ' : ', word)


traditional_words = []
def traditional_freq():
    traditional_text = open("../ProcessedData/out_traditional_lyrics.txt", 'r', encoding="utf-8")

    traditional_word = []
    for line in traditional_text.readlines():
        print("Yes")
        traditional_word.append(line)

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

    # for word in traditional_words_freq:
    #     print(traditional_words_freq[word], ' : ', word)


def pop_cloud(pop_words):
    pop_cloud_text = ''
    for word in pop_words:
        pop_cloud_text += ' '
        pop_cloud_text += word
    print(pop_cloud_text)
    generate_cloud(pop_cloud_text)
    


def generate_cloud(my_wordCloud):
    print('umad too')
    popWordCloud = WordCloud(font_path='Far_KoodkBd.ttf', background_color='white', height=4000, width=4000)
    popWordCloud.generate(my_wordCloud)
    plt.imshow(popWordCloud)
    plt.axis("off")

    plt.show()

pop_words = pop_freq()
traditional_freq()

pop_cloud(pop_words)

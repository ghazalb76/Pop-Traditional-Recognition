
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

    # for word in pop_words_freq:
    #     print(pop_words_freq[word], ' : ', word)


def traditional_freq():
    traditional_text = open("../ProcessedData/out_traditional_lyrics.txt", 'r', encoding="utf-8")

    traditional_word = []
    for line in traditional_text.readlines():
        print("Yes")
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

    # for word in traditional_words_freq:
    #     print(traditional_words_freq[word], ' : ', word)

pop_freq()
traditional_freq()
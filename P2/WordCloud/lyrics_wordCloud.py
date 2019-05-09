
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


pop_freq()
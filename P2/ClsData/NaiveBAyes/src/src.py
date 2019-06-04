import math
# print(3*math.log(4/40, 10)+math.log(3/40, 10))

def read_file():
    train_file = open("train.txt", 'r', encoding="utf-8")
    text = ""
    for line in train_file:
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
            print(word, len(word))
            if line[0] == "c1" and word != "c1" and word not in stopword_list and word != "\n":
                if word in pop_dict:
                    pop_dict[word] += 1
                else:
                    pop_dict[word] = 1
                if word in total_words_dict:
                    total_words_dict[word] += 1
                else:
                    total_words_dict[word] = 1

            elif line[0] == "c2" and word != "c2" and word not in stopword_list:
                if word in traditional_dict:
                    traditional_dict[word] += 1
                else:
                    traditional_dict[word] = 1
                if word in total_words_dict:
                    total_words_dict[word] += 1
                else:
                    total_words_dict[word] = 1
    print(pop_dict)


def naive_algo():
    pop_whole_words = 0
    for word in pop_dict:
        pop_whole_words += pop_dict[word]

    traditional_whole_words = 0
    for word in traditional_dict:
        traditional_whole_words += traditional_dict[word]

    for word in total_words_dict:
        if word in pop_dict:
            pop_freq_dict[word] = math.log((pop_dict[word]+1)/(pop_whole_words+len(total_words_dict)), 10)
        else:
            pop_freq_dict[word] = math.log((0+1)/(pop_whole_words+len(total_words_dict)), 10)
        if word in traditional_dict:
            traditional_freq_dict[word] = math.log((traditional_dict[word]+1)/(traditional_whole_words+len(total_words_dict)), 10)
        else:
            traditional_freq_dict[word] = math.log((0+1)/(traditional_whole_words+len(total_words_dict)), 10)


def read_test():
    test_file = open("test.txt", 'r', encoding="utf-8")
    for line in test_file:
        pop_prob = 0
        traditional_prob = 0
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
                pop_prob += pop_freq_dict[word]
                traditional_prob += traditional_freq_dict[word]
        print(pop_prob, traditional_prob)






pop_dict = {}
pop_freq_dict = {}
traditional_freq_dict = {}

traditional_dict = {}
total_words_dict = {}

stopword_list = []
unImportant = open("../../../WordCloud/stopwords.txt", 'r', encoding="utf-8")


for line in unImportant.readlines():
        stopword_list.append(line)
for sentence in stopword_list:
        stopword_list = sentence.split(' ')

read_file()
naive_algo()
read_test()
naive_probability()


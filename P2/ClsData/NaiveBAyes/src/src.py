import math

def read_train():
    train_file = open("../../train.txt", 'r', encoding="utf-8")
    text = ""
    for line in train_file:
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
            if line[0] == "pop" and word != "pop" and word not in stopword_list and word != "\n":
                if word in pop_dict:
                    pop_dict[word] += 1
                else:
                    pop_dict[word] = 1
                if word in total_words_dict:
                    total_words_dict[word] += 1
                else:
                    total_words_dict[word] = 1

            elif line[0] == "traditional" and word != "traditional" and word not in stopword_list:
                if word in traditional_dict:
                    traditional_dict[word] += 1
                else:
                    traditional_dict[word] = 1
                if word in total_words_dict:
                    total_words_dict[word] += 1
                else:
                    total_words_dict[word] = 1


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
        if word in traditional_dict:
            traditional_freq_dict[word] = math.log((traditional_dict[word]+1)/(traditional_whole_words+len(total_words_dict)), 10)

    pop_freq_dict['UNK'] = math.log((0+1)/(pop_whole_words+len(total_words_dict)), 10)
    traditional_freq_dict['UNK'] = math.log((0+1)/(traditional_whole_words+len(total_words_dict)), 10)


def read_test():
    out_text = ''
    test_file = open("../../test.txt", 'r', encoding="utf-8")
    for line in test_file:
        pop_prob = 0
        traditional_prob = 0
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
            if word != 'pop' and word != 'traditional' and word not in stopword_list:
                if word in pop_dict:
                    pop_prob += pop_freq_dict[word]
                    # print(word, pop_freq_dict[word])
                else:
                    pop_prob += pop_freq_dict['UNK']
                    # print(word, pop_freq_dict['UNK'])
                if word in traditional_dict:
                    traditional_prob += traditional_freq_dict[word]
                else:
                    traditional_prob += traditional_freq_dict['UNK']
        out_text += ' pop '+ str(pop_prob) +' traditional '+ str(traditional_prob)
    return out_text


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

read_train()
naive_algo()
out_text = read_test()

test_out = open("Test.output.txt", 'w', encoding="utf-8")
test_out.write(out_text)


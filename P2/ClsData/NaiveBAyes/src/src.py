import math


def read_stopwords():
    stopword_list = []
    unImportant = open("../../../WordCloud/stopwords.txt", 'r', encoding="utf-8")
    for line in unImportant.readlines():
            stopword_list.append(line)
    for sentence in stopword_list:
            stopword_list = sentence.split(' ')
    return stopword_list


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

        if traditional_prob > pop_prob:
            if line[0] == 'traditional' :
                # print('traditional --> traditional')
                traditional_measures['tp'] += 1
                pop_measures['tn'] += 1
            else :
                # print('pop --> traditional')
                traditional_measures['fp'] += 1
                pop_measures['fn'] += 1
        else :
            if line[0] == 'traditional':
                # print('traditional --> pop')
                traditional_measures['fn'] += 1
                pop_measures['fp'] += 1
            else :
                # print('pop --> pop')
                traditional_measures['tn'] += 1
                pop_measures['tp'] += 1

    pop_precision = pop_measures['tp'] / (pop_measures['tp'] + pop_measures['fp'])
    pop_recall = pop_measures['tp'] / (pop_measures['tp'] + pop_measures['fn'])
    pop_F1 = (2 * pop_precision * pop_recall) / (pop_precision + pop_recall)
    print ('Pop Precision : ', pop_precision*100)
    print ('Pop Recall : ', pop_recall*100)
    print ('Pop F1 : ', pop_F1*100)

    print()

    traditional_precision = traditional_measures['tp'] / (traditional_measures['tp'] + traditional_measures['fp'])
    traditional_recall = traditional_measures['tp'] / (traditional_measures['tp'] + traditional_measures['fn'])
    traditional_F1 = (2 * traditional_precision * traditional_recall) / (traditional_precision + traditional_recall)
    print ('Traditional Precision : ', traditional_precision*100)
    print ('Traditional Recall : ', traditional_recall*100)
    print ('Traditional F1 : ', traditional_F1*100)


    return out_text


total_words_dict = {}

pop_dict = {}
traditional_dict = {}

pop_freq_dict = {}
traditional_freq_dict = {}

pop_measures = {'tp':0, 'tn':0, 'fp':0, 'fn':0}
traditional_measures = {'tp':0, 'tn':0, 'fp':0, 'fn':0}

stopword_list = read_stopwords()
read_train()
naive_algo()
out_text = read_test()

test_out = open("Test.output.txt", 'w', encoding="utf-8")
test_out.write(out_text)


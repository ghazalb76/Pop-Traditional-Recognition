import math


def stopwords():
    stopword_list = []
    unImportant = open("../../WordCloud/stopwords.txt", 'r', encoding="utf-8")
    for line in unImportant.readlines():
            stopword_list.append(line)
    for sentence in stopword_list:
            stopword_list = sentence.split(' ')
    return stopword_list


def train(c1, c2):
    train_file = open("../../ClsData/TestCase/train.txt", 'r', encoding="utf-8")
    text = ""
    for line in train_file:
        line = line.rstrip()
        line = line.split(' ')
        if line[0] == 'c1':
            c1 += 1
        elif line[0] == 'c2':
            c2 += 1
        for word in line:
            if line[0] == 'c1' and word != 'c1' and word not in stopword_list and word != "\n":
                if word in pop_dict:
                    pop_dict[word] += 1
                else:
                    pop_dict[word] = 1
                if word in total_words_dict:
                    total_words_dict[word] += 1
                else:
                    total_words_dict[word] = 1

            elif line[0] == 'c2' and word != 'c2' and word not in stopword_list:

                if word in traditional_dict:
                    traditional_dict[word] += 1
                else:
                    traditional_dict[word] = 1
                if word in total_words_dict:
                    total_words_dict[word] += 1
                else:
                    total_words_dict[word] = 1
    return c1, c2


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


def test():
    out_text = ''
    measure_text = ''
    test_file = open("../../ClsData/TestCase/test.txt", 'r', encoding="utf-8")
    for line in test_file:
        pop_prob = math.log(c1/(c1+c2), 10)
        traditional_prob = math.log(c2/(c1+c2), 10)
        line = line.rstrip()
        line = line.split(' ')
        for word in line:
            if word != 'c1' and word != 'c2' and word not in stopword_list:
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
        out_text += ' c1 '+ str(pop_prob) +' c2 '+ str(traditional_prob) + '\n'

        if traditional_prob > pop_prob:
            if line[0] == 'c2' :
                # print('traditional --> traditional')
                traditional_measures['tp'] += 1
                pop_measures['tn'] += 1
            else :
                # print('pop --> traditional')
                traditional_measures['fp'] += 1
                pop_measures['fn'] += 1
        else :
            if line[0] == 'c2':
                # print('traditional --> pop')
                traditional_measures['fn'] += 1
                pop_measures['fp'] += 1
            else :
                # print('pop --> pop')
                traditional_measures['tn'] += 1
                pop_measures['tp'] += 1

    ''' Pop measures '''
    print(pop_measures['tp'], pop_measures['tn'], pop_measures['fp'], pop_measures['fn'])
    pop_accuracy = ((pop_measures['tp'] + pop_measures['tn'])/ (pop_measures['tp'] + pop_measures['tn'] + pop_measures['fp'] + pop_measures['fn']))
    pop_precision = pop_measures['tp'] / (pop_measures['tp'] + pop_measures['fp'])
    pop_recall = pop_measures['tp'] / (pop_measures['tp'] + pop_measures['fn'])
    pop_F1 = (2 * pop_precision * pop_recall) / (pop_precision + pop_recall)
    print ('c1 accuracy percentage : ', pop_accuracy*100)
    print ('c1 Precision percentage : ', pop_precision*100)
    print ('c1 Recall percentage : ', pop_recall*100)
    print ('c1 F1 percentage : ', pop_F1*100)
    measure_text += ('c1 accuracy percentage : ' + str(pop_accuracy*100) + '\n' +
                    'c1 Precision percentage : ' + str(pop_precision*100) + '\n' +
                    'c1 Recall percentage : ' + str(pop_recall*100) + '\n' +
                    'c1 F1 percentage : ' + str(pop_F1*100) + '\n\n')

    print()


    ''' Traditional measures '''
    # print(traditional_measures['tp'], traditional_measures['tn'], traditional_measures['fp'], traditional_measures['fn'])
    traditional_accuracy = ((traditional_measures['tp'] + traditional_measures['tn'])/ (traditional_measures['tp'] + traditional_measures['tn'] + traditional_measures['fp'] + traditional_measures['fn']))
    traditional_precision = traditional_measures['tp'] / (traditional_measures['tp'] + traditional_measures['fp'])
    traditional_recall = traditional_measures['tp'] / (traditional_measures['tp'] + traditional_measures['fn'])
    traditional_F1 = (2 * traditional_precision * traditional_recall) / (traditional_precision + traditional_recall)
    print ('c2 accuracy percentage : ', traditional_accuracy*100)
    print ('c2 Precision : ', traditional_precision*100)
    print ('c2 Recall : ', traditional_recall*100)
    print ('c2 F1 : ', traditional_F1*100)
    measure_text += ('c2 accuracy percentage : ' + str(traditional_accuracy*100) + '\n' +
                    'c2 Precision : ' + str(traditional_precision*100) + '\n' +
                    'c2 Recall : ' + str(traditional_recall*100) + '\n' +
                    'c2 F1 : ' + str(traditional_F1*100))


    return out_text, measure_text



total_words_dict = {}

pop_dict = {}
traditional_dict = {}

pop_freq_dict = {}
traditional_freq_dict = {}

pop_measures = {'tp':0, 'tn':0, 'fp':0, 'fn':0}
traditional_measures = {'tp':0, 'tn':0, 'fp':0, 'fn':0}

stopword_list = stopwords()
c1, c2 = train(0, 0)
naive_algo()
out_text, measure_text = test()

test_out = open("TestCase.output.txt", 'w', encoding="utf-8")
test_out.write(out_text)

test_out_report = open("TestCase.report.txt", 'w', encoding="utf-8")
test_out_report.write(measure_text)



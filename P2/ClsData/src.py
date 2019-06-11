import glob
import random


def label_pop(text_list):

    for pop_lyric_file in glob.glob("../ProcessedData/pop/*.txt"):
        txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
        for line in txt_file.readlines():
            text_list.append("pop "+ line) 
    return text_list


def label_traditional(text_list):

    for traditional_lyric_file in glob.glob("../ProcessedData/traditional/*.txt"):
        txt_file = open(traditional_lyric_file, 'r', encoding="utf-8")
        for line in txt_file.readlines():
            text_list.append("traditional "+ line)
    return text_list


def seperate_train_test(text_list):

    test_lines = []
    train_text = ''
    test_text = ''
    i = 0
    while i != int(0.2*len(text_list)):
        random_line = random.randint(0, len(text_list)-1)
        if text_list[random_line] not in test_lines:
            test_lines.append(text_list[random_line])
            i += 1
    for line in text_list:
        if line in test_lines:
            test_text += line
            test_lines.pop(test_lines.index(line))
        else:
            train_text += line
    print(i)
    return train_text, test_text


text_list = label_pop([])
text_list = label_traditional(text_list)
train_text, test_text = seperate_train_test(text_list)

train = open("train.txt", 'w', encoding="utf-8")
test = open("test.txt", 'w', encoding="utf-8")
train.write(train_text)
test.write(test_text)





def read_file():
    train_file = open("../train.txt", 'r', encoding="utf-8")
    text = ""
    words_list = []
    line_counter = 0
    new_line = ''
    cc = 0
    for line in train_file:
        line = line.rstrip()
        line = line.split(' ')
        line_counter += 1
        feature_counter = 0
        # new_line += str(line_counter) + ' '
        new_line += (line[0]+' ')
        for word in line:
            if word != line[0]:
                feature_counter += 1
                new_line += (word)
                new_line += (':'+str(1)+' ')
        new_line += '\n'
        line_counter += 1
        feature_counter = 0
        # new_line += str(line_counter) + ' '
        new_line += (line[0]+' ')
        for f in range(len(line)-1):
            if line[f] != line[0]:
                feature_counter += 1
                new_line += (line[f] +' '+ line[f+1])
                new_line += (':'+str(1)+' ')
        new_line += '\n'
        line_counter += 1
        feature_counter = 0
        # new_line += str(line_counter) + ' '
        new_line += (line[0]+' ')
        
        for word in line:
            if 'ان' in word or 'آن' in word:
                new_line += (':'+str(1)+' ')
                new_line += ('f_An')
        new_line += '\n'
        line_counter += 1
        feature_counter = 0
        # new_line += str(line_counter) + ' '
        new_line += (line[0]+' ')
        
        for word in line:
            if 'است' in word:
                new_line += (':'+str(1)+' ')
                new_line += ('f_An')
        new_line += '\n'


    return new_line

        

new_line = read_file()
# print(new_line)
with open("Mallet/input.train.txt", 'w', encoding="utf-8") as f:
    # Mallet/input.test.txt
    f.write(new_line)
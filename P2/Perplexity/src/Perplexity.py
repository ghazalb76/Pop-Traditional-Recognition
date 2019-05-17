import glob

uigram_pop_text = open("../../Model/pop/1gram.lm", 'r', encoding="utf-8")
unigram = []
for line in uigram_pop_text.readlines():
    line.rstrip("\n")
    unigram.append(line.split('|'))
for word in unigram:
    t = ''
    new = word[1]
    for i in range(0, len(word[1])-2):
        t += new[i]
    word[1] = t

text = ''
for pop_lyric_file in glob.glob("../../SplitData/train/pop/1.txt"):
    txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
    for line in txt_file.readlines():
        line = line.rstrip()
        line += ' </s> <s> '
        text += line

txt_file = open("oo.txt", 'w', encoding="utf-8")
txt_file.write(text)

print(text)
import glob



def label_pop(text):

    for pop_lyric_file in glob.glob("../ProcessedData/pop/*.txt"):
        txt_file = open(pop_lyric_file, 'r', encoding="utf-8")
        print(pop_lyric_file)
        for line in txt_file.readlines():
            text += "pop "+ line
    out.write(text)

out = open("out.txt", 'w', encoding="utf-8")
label_pop('')
import csv

# Read input
f=open("in_1.txt", encoding="utf8")
if f.mode == 'r':
    contents =f.read()
contents = contents.split()
print(contents)

# text_file = open("Output.txt", "w", encoding="utf8")

# Read dictionary
with open("Entries.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)
    for word in contents:
        for dWord in data:
            # print(word, "------>", dWord[1])
            if word == dWord[1]:
                print("YES")
                # text_file.write(dWord[0])



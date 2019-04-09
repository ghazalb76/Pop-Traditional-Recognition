import csv

def findSubString(str1, str2):
    print(str1.find(str2))

# Read input
f=open("in_1.txt", encoding="utf8")
if f.mode == 'r':
    contents =f.read()
contents = contents.split()

# text_file = open("Output.txt", "w", encoding="utf8")

# Read dictionary
with open("Entries.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)
    phonetics = []
    for word in contents:
        for dWord in data:
            if word == dWord[1]:
                phonetics.append(dWord[0])
                break
                # text_file.write(dWord[0])
jomle = ''
for t in phonetics:
    jomle+=t
print(jomle)
findSubString("football", " oot")
liste = []
for i in range(0, len(jomle)):
    sub = jomle[0:i]
    if any(sub in subl for subl in data):
        liste.append(sub)
liste.remove('')
print(liste)
dic = {}
for r in liste:
    dic[r] = []
print(dic)
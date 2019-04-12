import csv

def func(dic, jomle, data):
    flag = True
    for w in dic:
        for i in range(jomle.find(w)+len(w), len(jomle)+1):
            sub = jomle[jomle.find(w)+len(w):i]
            if jomle.find(w)+len(w) == len(jomle):
                flag = False
            # print(w, ':', jomle.find(w)+len(w), '----->', i, '    Sub Is ',sub)
            if any(sub in subl for subl in data) and sub not in dic[w] and sub is not '':
                dic[w].append(sub)




    for k in list(dic):
        for x in dic[k]:
            if x not in dic and x is not '':
                dic[x] = []
    return flag

# Read input
f=open("in_4.txt", encoding="utf8")
if f.mode == 'r':
    contents =f.read()
contents = contents.split()


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

jomle = ''
for t in phonetics:
    jomle+=t
print(jomle)
liste = []
for i in range(0, len(jomle)+1):
    sub = jomle[0:i]
    if any(sub in subl for subl in data) and sub is not '':
        liste.append(sub)

dic = {}
for r in liste:
    dic[r] = []


flag = True
for w in dic:
    for i in range(jomle.find(w)+len(w), len(jomle)+1):
        sub = jomle[jomle.find(w)+len(w):i]
        if any(sub in subl for subl in data) and sub is not '':
            dic[w].append(sub)

for k in list(dic):
    for x in dic[k]:
        if x not in dic and x is not '':
            dic[x] = []

while(flag):
    flag = func(dic, jomle, data)
w, h =10, 10
final = [[0 for x in range(w)] for y in range(h)] 

final.append("aa")
print(final)

print(dic)
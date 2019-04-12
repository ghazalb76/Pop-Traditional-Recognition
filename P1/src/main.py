import csv
from anytree import Node, RenderTree, PreOrderIter, LevelOrderGroupIter, PostOrderIter

class node():
    def __init__(self, name, parent, index):
        self.name = name
        self.parent = parent
        self.index = index
        self.children = []
        self.v = None

#######################################################################################################
# Read input
f=open("in_5.txt", encoding="utf8")
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
    if len(sub) != 1 and any(sub in subl for subl in data) and sub is not '':
        liste.append(sub)

############################################################################################################
root = node('root', None, -1)
word_obj = []
root.v = Node('root')
for r in liste:
    word = node(r, root, 0)
    word_obj.append(word)
    word.v = Node(r,root.v)




for word in word_obj:
    l = word.index+len(word.name)
    for i in range(l,len(jomle)+1):
        sub = jomle[l:i]
        if len(sub) != 1 and any(sub in subl for subl in data) and sub is not '':
            w = node(sub, word, l)
            word.children.append(w)
            word_obj.append(w)


for word in word_obj:
    for child in word.children:
        child.v = Node(child.name, word.v)




 

#####################################################################################
for pre, fill, node in RenderTree(root.v):
    print("%s%s" % (pre, node.name))


post = [node.name for node in PreOrderIter(root.v)]
for k in post:
    if jomle.find(k)+len(k) == len(jomle):
        r = k
        break

final_list = []
f=open("out_1.txt", 'w', encoding="utf8")
flag = False
for pre, fill, node in RenderTree(root.v):
    my_list = []
    if(node.name == r):
        node_p = node
        while(node_p.name != 'root'):
            my_list.append(node_p.name)
            node_p = node_p.parent
        my_list.reverse()
        print(my_list)
        de_phonetics = []
        count = 0
        for word in my_list:
            for dWord in data:
                if word == dWord[0]:
                    # print(word,'------------->',dWord)
                    de_phonetics.append(dWord[1])
                    count +=1
                    break
  
        if count >= len(my_list):
            print(de_phonetics)
            for de in de_phonetics:
                stri = ''
                stri += '['+de+']'
                f.write(stri)
        
            f.write('\n')
            
        # print(de_phonetics)
if any('mAd' in subl for subl in data):
    print("YESSSSSSSSSSSSSSSSSSSS")
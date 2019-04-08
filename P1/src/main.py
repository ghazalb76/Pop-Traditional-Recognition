import csv
with open("Entries.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)
f=open("in_1.txt", encoding="utf8")
if f.mode == 'r':
    contents =f.read()
contents = contents.split()
print(contents)
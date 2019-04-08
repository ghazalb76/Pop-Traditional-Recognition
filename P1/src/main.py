import csv
with open("Entries.csv", encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    data = []
    for row in reader:
        data.append(row)
import numpy as np


import glob
from shutil import copyfile

dirpath_pop = ["../../ProcessedData/pop\*.txt"]
dirpath_traditional = ["../../ProcessedData/traditional\*.txt"]

# Select all the pathes
files_path = []

pop_files_path = []
for path in dirpath_pop :
    for filename in glob.glob(path):
        pop_files_path.append(filename)
        files_path.append(filename)

traditional_files_path = []
for path in dirpath_traditional :
    for filename in glob.glob(path):
        traditional_files_path.append(filename)
        files_path.append(filename)

# Choose random files for test
random_num = len(files_path)*0.2
random_pathes = []
while (len(random_pathes) < random_num):
        random_path = np.random.choice(files_path, 1)
        if random_path not in random_pathes:
                random_pathes.append(random_path[0])

# Seperate train and test
test_pop_counter = 1
test_traditional_counter = 1
for i in random_pathes:
        if i in pop_files_path:
                pop_dest = "../test/pop/"+str(test_pop_counter)+".txt"
                copyfile(i, pop_dest)
                test_pop_counter += 1
        else:
                traditional_dest = "../test/traditional/"+str(test_traditional_counter)+".txt"
                copyfile(i, traditional_dest)
                test_traditional_counter += 1
        files_path.remove(i)

# Copy train files from Process part to split
test_pop_counter = 1
test_traditional_counter = 1
# print(files_path)
for train_path in files_path:
        print(train_path)
        if train_path in pop_files_path:
                pop_dest = "../train/pop/"+str(test_pop_counter)+".txt"
                copyfile(train_path, pop_dest)
                test_pop_counter += 1
        else:
                traditional_dest = "../train/traditional/"+str(test_traditional_counter)+".txt"
                copyfile(train_path, traditional_dest)
                test_traditional_counter += 1


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
random_pathes = np.random.choice(files_path, int(random_num))
test_pathes = np.split(random_pathes, 1)


# Seperate train and test
test_pop_counter = 1
test_traditional_counter = 1
for path in test_pathes:
        print(path)
        for i in path:
                if i in pop_files_path:
                        pop_dest = "../test/pop/"+str(test_pop_counter)+".txt"
                        copyfile(i, pop_dest)
                        test_pop_counter += 1
                        print(i)
                else:
                        traditional_dest = "../test/traditional/"+str(test_traditional_counter)+".txt"
                        copyfile(i, traditional_dest)
                        test_traditional_counter += 1
                print(i)
                files_path.remove(i)
                        

print(len(files_path), len(np.random.choice(files_path, int(random_num))))


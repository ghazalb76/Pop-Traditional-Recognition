import numpy as np


import glob
from shutil import copyfile

dirpath = ["../../ProcessedData/src.txt"]

destDirectory = "../new"

dest = "../p.txt"
files_path = []
for path in dirpath :
    for filename in glob.glob(path):
        files_path.append(filename)

random_num = len(files_path)*0.2
print(np.random.choice(files_path, int(random_num)))
print(len(files_path), len(np.random.choice(files_path, int(random_num))))


from distutils.command.config import config
import shutil
import sys
import os
from config import *
from sorter import Sorter

PATH = str(sys.argv[1])
Sorters : Sorter = []
ext : str = []

for line in folders[:-1]:
    ext.append(line)
    
Sorters.append(Sorter(ext, folders[-1]))
ext.clear()

for sorter in Sorters:
    if not os.path.exists(PATH + "/" + sorter.Folder):
        os.mkdir(PATH + "/" + sorter.Folder)

for sorter in Sorters:
    for ext in sorter.Extentions:
        for filename in os.listdir(PATH):
            if filename.endswith("." + ext):
                shutil.move(PATH + "/" + filename, PATH + "/" + sorter.Folder)
                continue
            else:
                continue


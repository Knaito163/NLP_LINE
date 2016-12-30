# -*- coding: utf-8 -*-
import glob
import sys
import os
from urllib.request import urlopen
import numpy as np
import pandas as pd


inputFolder = sys.argv[1]
inputFileList = glob.glob(inputFolder+"/*.txt")
output_folder = inputFolder + "_countResult"
# print(inputFolder, inputFileList, output_folder)

if os.path.isdir(output_folder)==False:
  os.system("mkdir "+ output_folder)
else:
  os.system("rm "+output_folder+"/*.csv")

for file in inputFileList:
  os.system("python3 count_spaceWord.py " + file + " " + output_folder)
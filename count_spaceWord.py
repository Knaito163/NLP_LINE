# -*- coding: utf-8 -*-
import glob
import sys
import os
from urllib.request import urlopen
#import numpy as np
import pandas as pd


file_name = sys.argv[1]

# stopワードの除去
stopword_path = "http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt"
stopword_file = urlopen(stopword_path)
stopwords_list = []
for line in stopword_file:
  stopwords = line.decode("utf-8").strip()
  if(stopwords != u""):
    stopwords_list.append(stopwords)
# 個人的な除去したいストップワード
private_stopword = ["。", "、",""]
for ps in private_stopword:
  stopwords_list.append(ps)
print(stopwords_list)

word_dict = {}
f = open(file_name, "r")
for line in f:
  word = line.split()
  for w in word:
    if(w not in stopwords_list):
      if(w not in word_dict):
        word_dict[w] = 1
        print("in")
      elif(w in word_dict):
        word_dict[w] += 1
        print("not in")
    else:
      print("Stop")
print(word_dict)
#降順で並び変えて表示
word_diclist = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
print(word_diclist)
setkey = []
setvalue = []
for wdl in word_diclist:
  #culmun
  setkey.append(wdl[0])
  setvalue.append(wdl[1])
print(setkey)
print(setvalue)

df_columns = ["単語", "出現数"]

df = pd.DataFrame(word_diclist, columns=df_columns)
df.to_csv("word_results.csv", mode="w")
# -*- coding: utf-8 -*-
import glob
import sys
import os
import re

def checkFunc(c_list):
  no_list = ["グループ通話が終了しました。\n", "[動画]\n", '[スタンプ]\n', '[ファイル]\n', '[アルバム]\n', "☎ chat.message.groupcall.started.long\n","[ノート]\n"]
  return False


# argv[1]でtextが入ってるinputフォルダ名を入力
folder_name = sys.argv[1]
# textファイルのpathをとってくる
path_list = glob.glob(folder_name+'/*.txt')


output_folder = "LINES_sentence_out"
if os.path.isdir(output_folder)==False:
  os.system("mkdir "+ output_folder)
else:
  os.system("rm "+output_folder+"/*.txt")

# すべての記事を音声ファイルへ変換してoutputフォルダに出力
cut_target = "\n"
j = 1
for path in path_list:
  f = open(path, "r")
  w_path = output_folder+"/" + path.rstrip(".txt").lstrip(folder_name+"/")
  w_path += "_lineout"+ str(j) +".txt"
  wf = open(w_path, "a")
  for line in f:
    l = re.split('[\t]',line)
    if(len(l)>2):
      if(l[2]!='[写真]\n' and l[2]!='[動画]\n' and l[2]!='[スタンプ]\n' and l[2]!='[ファイル]\n' and l[2].startswith('[アルバム]')!=True):
        for i in range(2,len(l)):
          print(i, l[i])
          wf.write(l[i])
    elif(len(l)<=2):
      for i in range(1,len(l)):
          print(i, l[i])
          wf.write(l[i])
  j += 1
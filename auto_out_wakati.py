#-*- coding: utf-8 -*-
import glob
import sys
import os


# argv[1]でtextが入ってるinputフォルダ名を入力
folder_name = sys.argv[1]
# textファイルのpathをとってくる
path_list = glob.glob(folder_name+'/*.txt')

#outputフォルダ作成
output_folder = folder_name +"_mecabwakati"
if os.path.isdir(output_folder)==False:
  os.system("mkdir "+ output_folder)

# すべてのparseしたLINEtxtをmecabで分かち書きしたファイルへ変換して出力
for path in path_list:
  cut_target = "/"
  f = path.split(cut_target)
  file_name = f[1]
  file_only_name = file_name.rstrip(".txt")
  # mecabのwakatiオプションで実行
  os.system("mecab -O wakati " + path + " -o " + output_folder +"/wakati_" + file_only_name +".txt")
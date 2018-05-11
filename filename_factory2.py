# coding:utf-8
#从filename_health.txt中读取文件名，生成filename_dm.txt为网页下载url
import sys
import os
import shutil

fileList = 'filename_health.txt'
newname ="filename_dm.txt"
save =open(newname,'w',encoding='utf-8')
filedir = open(fileList)
line = filedir.readline()
print(line)


while line:
    line = line.strip('\n')
    print(line)
    line = "http://dm-ecnu.org/insurance_get_ext_result/attr_get_" + line +".txt"
    print(line)
    print(line,file=save)
    line = filedir.readline()

# coding:utf-8
#从filename_raw.txt中读取文件名完整链接，生成filename_niubi.txt为简化文件名
import sys
import os
import shutil

fileList = 'filename_raw.txt'
targetDir = 'D:\\KG\\yiliao'
newname ="filename_niubi.txt"
save =open(newname,'a+',encoding='utf-8')
filedir = open(fileList)
line = filedir.readline()
print(line)


while line:
    line = line[32:]
    line = line.strip('\n')
    print(line)
    print(line,file=save)
    line = filedir.readline()

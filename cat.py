# coding:utf-8
#从filelist.txt中读取文件名，在本地查找对应txt,用于区分健康保险下的疾病保险和医疗保险
import sys
import os
import shutil

fileList = 'filelist.txt'
targetDir = 'D:\\KG\\yiliao'

filedir = open(fileList)
line = filedir.readline()
print(line)


while line:
    line = line[32:]
    line = line.strip('\n')
    line = line+'.txt'
    #print(line)
    basename = os.path.basename(line)
    exists = os.path.exists(line)
    if exists:
        shutil.copy(line, targetDir + '/' + basename)
    else:
        print
        line + ' not exists'

    line = filedir.readline()

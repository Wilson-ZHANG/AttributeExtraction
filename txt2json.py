#encoding: utf-8
#description: 将txt加工成json格式
from __future__ import print_function
import os
import re
import json
import csv


def produce_filename(targetdir):
    targetnames = os.listdir(targetdir)

    for name in targetnames:
        if '.txt' == name[-4:]:
            print("//"*20,name,"//"*20)
            print(name,'OK')
            attr_get(targetdir+"\\"+name)

def attr_get(filename):
    f = open(filename,'r',encoding='utf-8')
    newname ="clean_for_js_"+filename[-59:]
    print(newname)
    save =open(newname,'w',encoding='utf-8')

    #print(s)
    i = 0
    li = []
    context = []
    tmp =[]
    for line in f:
        line = line.strip('\n')
        save.write(line+' ')

    f.close()
    save.close()

    jsname = "js_"+filename[-59:]
    f_again = open(newname,'r',encoding='utf-8')
    save_again = open(jsname,'w',encoding='utf-8')
    s=f_again.read()
    #print(s)
    print('{',file=save_again)
    print('"filename":"',filename[-50:-4],'",',file=save_again)
    stt = s
    while(i<30):

        try:
            p_begin_attr = "ROUNDBEGIN " +"[\u4e00-\u9fa5]+"
            pattern_sub = "ROUNDEND "
            match_attr = re.search(p_begin_attr, stt, re.M)
            match_sub =re.search(pattern_sub,stt,re.M)
            entity = stt[match_attr.start()+11:match_attr.end()]
            print('"',entity,'":"',stt[match_attr.end()+1:match_sub.start()-1],'",',file=save_again)
            stt = stt[match_sub.end():]

        except:
            pass
        i+=1
    print("}", file=save_again)

produce_filename('D:\\KG\\attr_get_new_yiliao')

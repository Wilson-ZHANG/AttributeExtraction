#encoding: utf-8
#description: 将attr_get_txt加工成json格式
from __future__ import print_function
import os
import re


def produce_filename(targetdir):
    targetnames = os.listdir(targetdir)
    for name in targetnames:
        if '.txt' == name[-4:]:
            print("//"*20,name,"//"*20)
            print(name,'OK')
            attr_get(targetdir+"\\"+name)

def attr_get(filename):
    f = open(filename,'r',encoding='utf-8')
    newname ="txt2js_"+filename[-59:]
    print(newname)
    save =open(newname,'w',encoding='utf-8')
    s =f.read()
    print(s)
    i = 0
    while(i<79):
        try:
            #print(data_set[i])
            #pattern = flag + "\s*"+str(data_set[i])+"(\n|\s)*[\u4e00-\u9fa5]*(\n|\s)*"+flag
            p_begin = "ROUNDBEGIN "
            p_begin_attr = "ROUNDBEGIN " +"[\u4e00-\u9fa5]+"
            pattern_sub = "ROUNDEND "
            match = re.search(p_begin,s,re.M)
            match_attr = re.search(p_begin_attr, s, re.M)
            match_sub =re.search(pattern_sub,s,re.M)
            print("match",match)
            print("match_attr", match_attr)
            print("match_sub",match_sub)
            begin = match.end()
            entity = s[match.end():match_attr.end()]
            print('{"',entity,'":"',s[match_attr.end()+2:match_sub.start()],'"}',file=save)
            print('begin=',begin)
            final = match_sub.end()
            print('final=', final)
            s =s[match_sub.end():]

        except:
            pass
        i+=1
    save.close()
    f.close()

produce_filename('D:\\KG\\testa')

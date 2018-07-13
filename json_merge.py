#encoding: utf-8
#description: 将attr_get_txt加工成json格式
from __future__ import print_function
import os
import re
import json
import csv


def produce_filename(targetdir):
    targetnames = os.listdir(targetdir)
    jsname = "disease_with_time.json"

    for name in targetnames:
        if '.txt' == name[-4:]:
            print("//"*20,name,"//"*20)
            print(name,'OK')
            attr_get(targetdir+"\\"+name,jsname)

def attr_get(filename,jsname):
    f = open(filename,'r',encoding='utf-8')
    f2 = open(jsname, 'a+', encoding='utf-8')
    s = f.read()
    s = '{'+s[2:-4]+'}'
    print(s,file=f2)


produce_filename('D:\\KG\\js_jibing')

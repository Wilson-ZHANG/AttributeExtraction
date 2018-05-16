#encoding: utf-8
#description: 将医疗和疾病的属性粗抽取的结果改写成json格式
#date: 2018-05-10
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
    newname ="attr_get_"+filename[-50:]
    #print(newname)
    save =open(newname,'a+',encoding='utf-8')
    s =f.read()
    #print('s:',s)
    #patterns = "[\u4e00-\u9fa5]+\[[\d*\]][\u4e00-\u9fa5]+"
    i = 0
    #jibing

    data_set = ["投保范围", "等待期", "重大疾病保险金", "身故保险金", "重大疾病的范围", "是否有多次给付",
              "犹豫期", "责任免除", "保险期间", "续保", "缴费方式", "观察期", "重大疾病保险金给付日",
              "给付总额的保证", "基本保险金额的变更", "保险费率的调整", "宽限期", "保单贷款政策",
              "退保/解除合同", "首个重大疾病保险金给付日", "自动垫交保险费", "保单备案时间"]

    #yiliao
    '''
    data_set= ["投保范围", "保险期间", "等待期", "缴费方式", "保险责任", "住院费用和门诊费用的范围",
              "保单年度累计给付限额（年限额）", "所有保险期间内最高给付限额（最高给付金额）", "每日给付限额（日限额）",
              "保单年度内累计最高给付日数", "住院及手术医疗保险金", "门诊医疗保险金", "是否存在保额提升情况",
              "责任免除", "保险人不同意续保下", "续保", "无保险事故优惠", "保险事故通知时间", "保险费率的调整",
              "合同终止与满期之间间隔限制", "合作医院", "预授权", "未及时核定补偿", "险种转换", "自动垫交保险费", "保单备案时间"]
    '''
    while(i<data_set.__len__()):
        print('ROUNDBEGIN', data_set[i], file=save)
        try:
            pattern = "\d([.]\d)+\s+"+str(data_set[i])+"\s+[\u4e00-\u9fa5]+\s*"
            match = re.search(pattern,s,re.M)
            begin = match.start()
            start = match.end()
            match1 = re.search("\d[.]\d*\s+[\u4e00-\u9fa5]+", s[start:], re.M)
            end = match1.start()
            print(s[begin:end + start],file=save)
        except:
            pass
        try:
            pattern = "第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十)\s*条(\n|\s)+"+str(data_set[i])+"(\n|\s)+[\u4e00-\u9fa5]+\s*"
            pattern_sub = "第(一|二|三|四|五|六|七|八|九|十|十一|十二|十三|十四|十五|十六|十七|十八|十九|二十|二十一|二十二|二十三|二十四|二十五|二十六|二十七|二十八|二十九|三十)\s*条(\n|\s)+"
            match = re.search(pattern,s,re.M)
            begin = match.start()
            start = match.end()
            match1 = re.search(pattern_sub, s[start:], re.M)
            end = match1.start()
            print(s[begin:end + start], file=save)
        except:
            pass
        try:
            while(s):
                p1 = data_set[i]
                match_brute =re.search(p1,s)
                print(s[match_brute.start()-10:match_brute.end()+10],file=save)
                t = s[match_brute.end():]
                cnt = match_brute.end()
                while(t):
                    make = re.search(p1,t,re.M)
                    print(s[cnt+make.start()-20:cnt+make.end()+30],file=save)
                    t = t[make.end():]
                    cnt +=make.end()

                #print(ss[match_brute.start()- 20:match_brute.end()+ 30],file=save)
        except:
            pass
        print('ROUNDEND', data_set[i], file=save)
        i+=1
    save.close()
    f.close()
produce_filename('D:\\KG\\testa')
#attr_get('D:\\PyCharmProjects\\attrifind\\test\\健康保险_疾病保险\\.txt')

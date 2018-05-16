import re
import os

def produce_filename(targetdir):
    targetnames = os.listdir(targetdir)
    for name in targetnames:
        if '.txt' == name[-4:]:
            print("//"*20,name,"//"*20)
            print(name,'OK')
            attr_get(targetdir+"\\"+name)

def attr_get(filename):
    f = open(filename, 'r', encoding='utf-8')
    newname = "attr_get_" + filename[-50:]
    print(newname)
    save = open(newname, 'a+', encoding='utf-8')
    data_set = ["投保范围", "保险期间", "等待期", "缴费方式", "保险责任", "住院费用和门诊费用的范围",
                "保单年度累计给付限额（年限额）", "所有保险期间内最高给付限额（最高给付金额）", "每日给付限额（日限额）",
                "保单年度内累计最高给付日数", "住院及手术医疗保险金", "门诊医疗保险金", "是否存在保额提升情况",
                "责任免除", "保险人不同意续保下", "续保", "无保险事故优惠", "保险事故通知时间", "保险费率的调整",
                "合同终止与满期之间间隔限制", "合作医院", "预授权", "未及时核定补偿", "险种转换", "自动垫交保险费", "保单备案时间"]
    ss = f.read()
    #print(ss)
    i = 0
    while(i<data_set.__len__()):
        print("****"*10,data_set[i],"****"*10)
        print(data_set.__len__())
        try:
            while(ss):
                p1 = data_set[i]
                match_brute =re.search(p1,ss)
                print(ss[match_brute.start()-10:match_brute.end()+10],file=save)
                t = ss[match_brute.end():]
                cnt = match_brute.end()
                while(t):
                    make = re.search(p1,t,re.M)
                    print(ss[cnt+make.start()-20:cnt+make.end()+30],file=save)
                    t = t[make.end():]
                    cnt +=make.end()

                #print(ss[match_brute.start()- 20:match_brute.end()+ 30],file=save)
        except:
            pass
        i+=1



produce_filename('D:\\KG\\testa')

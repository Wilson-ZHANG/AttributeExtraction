#encoding: utf-8
#description: 从字符串中提取省市县等名称,用于从纯真库中解析解析地理数据
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
    newname ="flag_"+filename[-59:]
    #print(newname)
    save =open(newname,'a+',encoding='utf-8')
    s =f.read()
    print(filename[31:-4],file=save)
    i = 0
    data_set = ["保险责任", "责任免除","保险事故", "保险费", "保险期间", "解除合同", "保险金给付", "保险金额",
                "保险事故通知", "犹豫期", "效力恢复", "宽限期", "投保范围", "续保","缴费方式",
                "疾病身故保险金","护理保险金","健康护理保险金","长寿护理保险金","健康维护保险金",
                "观察期","最低保证利率","保单贷款政策","部分领取","等待期","保险金额计算方式",
                "保险费率的调整","宽限期","退保","自动垫交保险费","重大疾病保险金","身故保险金","重大疾病的范围",
                "是否有多次给付","重大疾病保险金给付日","给付总额的保证","基本保险金额的变更",
                "退保/解除合同","首个重大疾病保险金给付日","承保人群","重度失能保险金","一般失能保险金",
                "身体全残保险金","一般失能的范围","重度失能的范围","保费豁免","给付标准和保险期间的关系",
                "减保","减保（减额交清保险）","减额交清保险","身故给付","身故给付（可能以特殊退费形式）",
                "可能以特殊退费形式","定期复查","保单年度累计给付限额","保单年度累计给付限额（年限额）",
                "年限额","所有保险期间内最高给付限额","所有保险期间内最高给付限额（最高给付金额）",
                "最高给付金额","每日给付限额","每日给付限额（日限额）","日限额","保单年度内累计最高给付日数",
                "住院及手术医疗保险金","门诊医疗保险金","参加社会医疗保险","社保补偿","是否存在提额情况",
                "保险人不同意续保下","住院费用和门诊费用的范围","无保险事故优惠","保险事故通知时间","合同终止与满期之间间隔限制",
                "合作医院","预授权","未及时核定补偿","险种转换"]
    while(i<79):
        try:
            #print(data_set[i])
            #pattern = flag + "\s*"+str(data_set[i])+"(\n|\s)*[\u4e00-\u9fa5]*(\n|\s)*"+flag
            pattern = "ROUNDBEGIN" +"\s*"+str(data_set[i])
            pattern_sub = "ROUNDEND" +"\s*"+str(data_set[i])
            match = re.search(pattern,s,re.M)
            match_sub =re.search(pattern_sub,s,re.M)
            #print("match",match)
            #print("match_sub",match_sub)
            begin = match.end()
            print('begin=',begin)
            final = match_sub.end()
            print('final=', final)
            #print(s[begin:final])
            match1 = re.search("[\u4e00-\u9fa5]*(\d)+日(内)*",s[begin:final], re.M)
            print("match1",match1)
            print(match1.start(),match1.end())
            print('CLEAR',data_set[i],s[begin+match1.start():begin+match1.end()],file=save)

        except:
            pass
        i+=1
    save.close()
    f.close()
produce_filename('D:\\KG\\yiliao_attr_get')
#attr_get('D:\\PyCharmProjects\\attrifind\\test\\健康保险_疾病保险\\.txt')
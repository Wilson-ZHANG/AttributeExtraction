#encoding: gbk
import re

def tiny_calculate_word(filename):
    content = {}
    save = open(filename, 'a+', encoding='gbk')
    with open(filename, 'r+') as fr:
        for line in fr.readlines():
            if line not in content:
                content[line] = 0
            content[line] += 1
    for word, val in content.items():
        print(word, val, file=save)

filename = "medicare_edit.json"

pattern = '"[\u4e00-\u9fa5]+": "[\u4e00-\u9fa5]+"'
pattern_mid = '": "'
f = open(filename, 'r', encoding='utf-8')
filename_li = []
flag = False
cc = 0 #trick and stupid method to save attribute name
for line in f.readlines():
    #print(line)
    s = str(line)
    try:
        match = re.search(pattern,s,re.M)
        match_mid = re.search(pattern_mid,s,re.M)
        filename_head = match.start()+1
        filename_tail = match_mid.start()
        value_head = match_mid.end()
        value_tail = match.end()-1
        #print(s[filename_head:filename_tail]," HAVE ",s[value_head:value_tail])
        new_filename = s[filename_head:filename_tail]+'.txt'
        for item in filename_li:
            if(item == new_filename):
                flag = True
        if(flag == False):
            filename_li.append(new_filename)

        with open(new_filename, 'a+') as f:
             f.write(s[value_head:value_tail]+'\n')
             print("write by ",new_filename)
        #print(str(line)[match.start():match.end()])
        flag = False

    except:
        pass




for name in filename_li:
    tiny_calculate_word(name)



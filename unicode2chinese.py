# -*- coding: utf-8 -*-
import json

#a = '\u64cd\u4f5c\u7cfb\u7edf'
#print(a.encode("utf-8").decode("utf-8"))
input_file = 'zstp_tree.json'
def extract_name(input_file):
    name_list = []
    try:
        with open(input_file, encoding='utf-8') as f:
            for line in f:
                r = json.loads(line, strict=False)
                for i in range(27575):
                    try:
                        temp_name = r['nodes'][i]['name'].encode("utf-8").decode("utf-8")
                        name_list.append(temp_name)
                        #print(temp_name)
                    except:
                        pass
    except:
        pass
    return name_list
kk = []
kk = extract_name(input_file)

print(kk.__len__())
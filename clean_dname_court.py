# -*- coding: utf-8 -*-
import re

#filename = 'id_court.csv'
filename = 'zhong_thousand_sample_4_entity_id_dname.csv'
#filename = 'stupid_english.csv'
#save = open('id_court_class.csv','a+',encoding='utf-8')i
save = open('zhong_id_court.csv','a+',encoding='utf-8')
#save = open('magic_time.csv','a+',encoding='utf-8')


regax = '[\u4e00-\u9fa5]*?法院'
pattern1 = re.compile(regax)
regax2 = '((法院|刑|附带)([\u4e00-\u9fa5]*?)书)'
pattern2 = re.compile(regax2)
number_regax ='[0-9]*,'
pattern_number = re.compile(number_regax)
cnt =0
with open(filename,'r',encoding='utf-8') as f:
    for line in f:
        s = line
        #print('s:',s)

        #print(pattern1.search(s).group())
        try:
            print(pattern_number.search(s).group(0)+pattern1.search(s).group()+','+pattern2.search(s).group(3),file=save)
            #print("法院：",pattern1.search(s).group(),file=save)
            #print(pattern1.search(s))

            #print(pattern2.search(s))
        except:
            if(cnt ==12):
                print(line+'ERRRRRRRRRRRROR',file=save)
            else:
                print('id,court,class',file=save)
                cnt = 12
        
        

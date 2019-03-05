'''
20190219
修正裁判文书案号的标点符号
将所有英文的括弧()替换为中文的括弧（）
将所有中文的中括号【】替换为英文的中括号[]

20190220
修正抽取结果中的案号

'''
import re
cnt = 0
#filename = "punc_test.csv"
#filename = "wenshu_with_id_entity_id_case_ok.csv"
filename = 'zhong_thousand_sample_4_entity_id_case.csv'
newname1 = filename[:-4] + '_clean_second.csv'
save1 = open(newname1, 'a+', encoding='utf-8')
pattern1 = re.compile('([\u4e00-\u9fa5]+书（)')
pattern2 = re.compile('(原本（)')
pattern3 = re.compile('(（原本）（)')
with open(filename,encoding='utf-8') as f:
    for line in f:
        line = line.replace('事务所律师', '事务所')
        # print(line)
        line = line.replace('(', '（')
        # print(line)
        line = line.replace(')', '）')
        line = re.sub(pattern1,'（',line)
        line = re.sub(pattern2, '（', line)
        line = re.sub(pattern3, '（', line)
        if(cnt  % 1000 == 0):
            print(cnt)
        print(line[:-1],file=save1)
        cnt+=1

save1.close()

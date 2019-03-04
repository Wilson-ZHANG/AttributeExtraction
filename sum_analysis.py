import csv
import re

cancer_cnt_main = 0
cancer_cnt_ad = 0
serious_cnt_main = 0
serious_cnt_ad = 0
others_cnt_main = 0
others_cnt_ad = 0
cost_cnt_main = 0
cost_cnt_ad = 0
quote_cnt_main = 0
quote_cnt_ad = 0

filename1 = 'cost_cnt_in_ad.csv'
save = open(filename1,'a+',encoding='utf-8')
filename2 = 'quote_cnt_in_ad.csv'
save2 = open(filename2,'a+',encoding='utf-8')
f = open('filename_disease_main.csv', encoding='utf-8')

df1 = 'cancer_cnt_in_ad.csv'
dsave1 = open(df1,'a+',encoding='utf-8')
df2 = 'others_cnt_in_ad.csv'
dsave2 = open(df2,'a+',encoding='utf-8')
df3 = 'serious_cnt_in_ad.csv'
dsave3 = open(df3,'a+',encoding='utf-8')
csvreader = csv.reader(f)
disease_main_list = list(csvreader)

file1 = 'disease_old_orgainzed.csv'
end_save1 = open(file1,'a+',encoding='utf-8')
file2 = 'medicare_old_organized.csv'
end_save2 = open(file2,'a+',encoding='utf-8')

f = open('filename_medicare_main.csv', encoding='utf-8')
csvreader = csv.reader(f)
medicare_main_list = list(csvreader)

f = open('filename_disease_ad.csv', encoding='utf-8')
csvreader = csv.reader(f)
disease_ad_list = list(csvreader)

f = open('filename_medicare_ad.csv', encoding='utf-8')
csvreader = csv.reader(f)
medicare_ad_list = list(csvreader)

f = open('filename_cancer.csv', encoding='utf-8')
csvreader = csv.reader(f)
cancer_list = list(csvreader)
f = open('filename_others.csv', encoding='utf-8')
csvreader = csv.reader(f)
others_list = list(csvreader)
f = open('filename_serious.csv', encoding='utf-8')
csvreader = csv.reader(f)
serious_list = list(csvreader)
f = open('filename_quote.csv', encoding='utf-8')
csvreader = csv.reader(f)
quote_list = list(csvreader)
f = open('filename_cost.csv', encoding='utf-8')
csvreader = csv.reader(f)
cost_list = list(csvreader)

for t in disease_main_list:
    for cancer in cancer_list:
        if(re.search(t[0],cancer[0],re.M)):
            print(cancer[0],file=end_save1)
            cancer_cnt_main+=1
    for others in others_list:
        if (re.search(t[0], others[0], re.M)):
            print(others[0],file=end_save1)
            others_cnt_main += 1
    for serious in serious_list:
        if (re.search(t[0], serious[0], re.M)):
            print(serious[0],file=end_save1)
            serious_cnt_main += 1

print(cancer_cnt_main,'cancer cnt in main \n')
print(others_cnt_main,'others cnt in main \n')
print(serious_cnt_main,'serious cnt in main \n')


for t in medicare_main_list:
    for cost in cost_list:
        if(re.search(t[0],cost[0],re.M)):
            print(cost[0],file=end_save2)
            cost_cnt_main+=1
    for quote in quote_list:
        if (re.search(t[0], quote[0], re.M)):
            print(quote[0],file=end_save2)
            quote_cnt_main += 1

print(cost_cnt_main,'cost cnt in main \n')
print(quote_cnt_main,'quote cnt in main \n')

for t in disease_ad_list:
    for cancer in cancer_list:
        if(re.search(t[0],cancer[0],re.M)):
            print(cancer[0],file=end_save1)
            cancer_cnt_ad +=1
    for others in others_list:
        if (re.search(t[0], others[0], re.M)):
            print(others[0],file=end_save1)
            others_cnt_ad += 1
    for serious in serious_list:
        if (re.search(t[0], serious[0], re.M)):
            print(serious[0],file=end_save1)
            serious_cnt_ad += 1

print(cancer_cnt_ad,'cancer cnt in ad \n',file=dsave1)
print(others_cnt_ad,'others cnt in ad \n',file=dsave2)
print(serious_cnt_ad,'serious cnt in ad \n',file=dsave3)


for t in medicare_ad_list:
    for cost in cost_list:
        if(re.search(t[0],cost[0],re.M)):
            print(cost[0],file=end_save2)
            cost_cnt_ad +=1
    for quote in quote_list:
        if (re.search(t[0], quote[0], re.M)):
            print(quote[0],file=end_save2)
            quote_cnt_ad += 1

print(cost_cnt_ad,'cost cnt in ad \n')
print(quote_cnt_ad,'quote cnt in ad \n')
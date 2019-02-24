import csv
import re

filename1 = 'cancer_new.csv'
save1 = open(filename1,'a+',encoding='utf-8')
filename2 = 'serious_new.csv'
save2 = open(filename2,'a+',encoding='utf-8')
filename3 = 'others_new.csv'
save3 = open(filename3,'a+',encoding='utf-8')
filename4 = 'cost_new.csv'
save4 = open(filename4,'a+',encoding='utf-8')
filename5 = 'quote_new.csv'
save5 = open(filename5,'a+',encoding='utf-8')


c = 'disease_title.json'
save_c = open(c,'a+',encoding='utf-8')
f = open('disease_old_orgainzed.csv', encoding='utf-8')
csvreader = csv.reader(f)
disease_list = list(csvreader)

f = open('medicare_old_organized.csv', encoding='utf-8')
csvreader = csv.reader(f)
medicare_list = list(csvreader)

f = open('cancer.csv', encoding='utf-8')
csvreader = csv.reader(f)
cancer_list = list(csvreader)
f = open('others.csv', encoding='utf-8')
csvreader = csv.reader(f)
others_list = list(csvreader)
f = open('serious.csv', encoding='utf-8')
csvreader = csv.reader(f)
serious_list = list(csvreader)
f = open('quote.csv', encoding='utf-8')
csvreader = csv.reader(f)
quote_list = list(csvreader)
f = open('cost.csv', encoding='utf-8')
csvreader = csv.reader(f)
cost_list = list(csvreader)

#print(cancer_list[0][0]+','+cancer_list[0][1]+','+cancer_list[0][2]+','+cancer_list[0][3]+','+cancer_list[0][4]+','+cancer_list[0][5]+','+cancer_list[0][6]+','+cancer_list[0][7]+','+cancer_list[0][8]+','+cancer_list[0][9]+','+cancer_list[0][10]+','+cancer_list[0][11]+','+cancer_list[0][12],file=save1)
#print(cost_list[0][0]+','+cost_list[0][1]+','+cost_list[0][2]+','+cost_list[0][3]+','+cost_list[0][4]+','+cost_list[0][5]+','+cost_list[0][6]+','+cost_list[0][7]+','+cost_list[0][8]+','+cost_list[0][9]+','+cost_list[0][10]+','+cost_list[0][11]+','+cost_list[0][12],file=save2)
cnt = 0
for cancer in cancer_list:
    for d in disease_list:
        if(d[0] == cancer[12] ):
            cnt = 1
    if(cnt ==0):
            print(cancer[0]+','+cancer[1]+','+cancer[2]+','+cancer[3]+','+cancer[4]+','+cancer[5]+','+cancer[6]+','+cancer[7]+','+cancer[8]+','+cancer[9]+','+cancer[10]+','+cancer[11]+','+cancer[12],file=save1)
    cnt = 0
for serious in serious_list:
    for d in disease_list:
        if (d[0] == serious[12]):
            cnt = 1
    if (cnt == 0):
            print(serious[0]+','+serious[1]+','+serious[2]+','+serious[3]+','+serious[4]+','+serious[5]+','+serious[6]+','+serious[7]+','+serious[8]+','+serious[9]+','+serious[10]+','+serious[11]+','+serious[12],file=save2)
    cnt = 0
for others in others_list:
    for d in disease_list:
        if (d[0] == others[12]):
            cnt = 1
    if (cnt == 0):
            print(others[0]+','+others[1]+','+others[2]+','+others[3]+','+others[4]+','+others[5]+','+others[6]+','+others[7]+','+others[8]+','+others[9]+','+others[10]+','+others[11]+','+others[12],file=save3)
    cnt = 0

for cost in cost_list:
    for m in medicare_list:
        if(m[0] == cost[12]):
            cnt = 1
    if(cnt == 0):
        print(cost[0]+','+cost[1]+','+cost[2]+','+cost[3]+','+cost[4]+','+cost[5]+','+cost[6]+','+cost[7]+','+cost[8]+','+cost[9]+','+cost[10]+','+cost[11]+','+cost[12],file=save4)
    cnt = 0
for quote in quote_list:
    for m in medicare_list:
        if (m[0] == quote[12]):
            cnt = 1
    if (cnt == 0):
        print(quote[0]+','+quote[1]+','+quote[2]+','+quote[3]+','+quote[4]+','+quote[5]+','+quote[6]+','+quote[7]+','+quote[8]+','+quote[9]+','+quote[10]+','+quote[11]+','+quote[12],file=save5)
    cnt = 0
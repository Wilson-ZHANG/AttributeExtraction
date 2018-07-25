
disease_li = []
medicare_li = []
product_li = []

with open("disease_edit_filename.txt",'r') as f1:
    for line in f1:
        disease_li.append(line.strip().split('\n'))
with open("medicare_edit_filename.txt",'r') as f2:
    for line in f2:
        medicare_li.append(line.strip().split('\n'))

#for i in disease_li:
 #   print(i)
#for j in medicare_li:
 #   print(j)
#print(medicare_li[0][0])
#print(medicare_li.__len__())
save = open("product_status_reset_version_all.txt",'w')
with open("product_status_filename_all.txt",'r+') as f:
    for line in f:
        product_li.append(line.strip().split('\t'))
#print(product_li[0][0])
print(product_li[1][1])
cnt = 0
count_pro = 0
while(cnt < product_li.__len__()):
    flag = False
    for i in range(0,disease_li.__len__()):
        if(disease_li[i][0] == product_li[cnt][0]):
            flag = True
    for j in range(0,medicare_li.__len__()):
        if(medicare_li[j][0] == product_li[cnt][0]):
            flag = True
    if(flag == False and product_li[cnt][1] == '1'):
        product_li[cnt][1] = '0'
        #print(product_li[cnt])
        count_pro +=1
    cnt += 1
#print(count_pro)
for line in product_li:
    print(line[0],line[1],file=save)
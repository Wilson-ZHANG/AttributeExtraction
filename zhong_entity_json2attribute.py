import json

filename = "zhong_thousand_sample_4_entity.json"
newname1 = filename[:-5] + '_id_dname.csv'
save1 = open(newname1, 'a+', encoding='utf-8')
print('id,document',file=save1)
newname2 = filename[:-5] + '_id_case.csv'
save2 = open(newname2, 'a+', encoding='utf-8')
print('id,case_number,past',file=save2)
#newname3 = filename[:-5] + '_id_content.csv'
#save3 = open(newname3, 'a+', encoding='utf-8')
#print('id,fact,law,result',file=save3)
with open(filename,encoding='utf-8') as f:
    for line in f:
        #print(type(line))
        r = json.loads(line, strict=False)
        try:
            id = r['id']
            print(id,type(id))
        except:
            pass
        try:
            print(str(id)+','+r['文书官方名称'],file=save1)
        except:
            print("No.",id,"faced error in id_dname.csv")
        try:
            print(str(id)+','+r['案号']+','+r['关联案号'],file=save2)
        except:
            print("No.", id, "faced error in id_case.csv")
   #     try:
  #          print(str(id)+','+r['经审理查明（证据核实）']+','+r['法律法规与司法解释']+','+r['判决如下'],file=save3)
 #       except:
 #           print("No.", id, "faced error in id_content.csv")
#save3.close()
save2.close()
save1.close()
fa = 'new_sample_2.json'
newname = fa[:-5] + '_id_title.csv'
save = open(newname, 'a+', encoding='utf-8')
with open(fa,encoding='utf-8') as f:
    for line in f:
        #print(type(line))
        rx = json.loads(line, strict=False)
        try:
            id = r['id']
            print(id)
        except:
            pass
        try:
            print(r['id']+','+r['title'],file=save)
        except:
            print("No.", id, "faced error in id_title.csv")

save.close()

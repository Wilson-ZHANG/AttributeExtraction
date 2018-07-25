##encoding: gbk
filename = "test.txt"

content = {}
save = open(filename, 'a+', encoding='gbk')
with open(filename, 'r+') as fr:
    for line in fr.readlines():
        if line not in content:
            content[line] = 0
        content[line] += 1
for word, val in content.items():
    print(word, val,file=save)
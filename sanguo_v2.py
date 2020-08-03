import re
def find_item(hero):
    with open('sanguo.txt',encoding='utf-8') as f:
        data = f.read().replace('\n','')
        name_num = re.findall(hero,data)
        print('主角 %s 出现 %s 次' %(hero,len(name_num)))

    return name_num


name_dict = {}
with open('name.txt',encoding='utf-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
           name_num = find_item(n)
           name_dict[n] = name_num
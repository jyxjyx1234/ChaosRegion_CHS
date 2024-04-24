import json
import os

namelist=[]
datanames = os.listdir('.\OriginFile\\rld_processed')#改地址
for dataname in datanames:
    if os.path.splitext(dataname)[1] == '.json':
        with open('.\OriginFile\\rld_processed\\'+dataname,'r',encoding='utf8') as f:
            f=json.load(f)
        for dic in f:
            if 'name' in dic:
                if dic['name'] not in namelist:
                    namelist.append(dic['name'])
with open('namelist.txt','w',encoding='utf8') as f:
    for i in namelist:
        f.write(i+'\n')
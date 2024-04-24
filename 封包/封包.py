#将译文与原文的二进制相对应并替换
import os
import json
from 文本处理 import wenbenchuli,hanzitihuan#用于处理译文
from namedict import namedict

#测试用，从galtransl目录中拉取译文
#os.system('copy "D:\\aPrograms\GALTRANS\钢炎\\transl_cache\\*.json" "D:\鋼炎のソレイユ_chs\译文\\"')
##尝试用gbk编码进行写入时，无效掉wenbenchuli
outencode='gbk'
if outencode!='sjis':
    def wenbenchuli(i):
        return i
    def hanzitihuan(i):
        return i

def tihuan(oridata,start,end,replaced):#将oridata中start到end区间的内容替换为replaced的内容
    oridata1=oridata[0:start]
    oridata2=replaced
    oridata3=oridata[end:]
    return oridata1+oridata2+oridata3

#替换默认字体
zititihuan=False#替换字体疑似毫无作用
ori_font='ＭＳ Ｐゴシック'#ＭＳ Ｐゴシック
changed_font='WenQuanYi Micro Hei'
bori_font=ori_font.encode(encoding='sjis')
bchanged_font=changed_font.encode(encoding='sjis')
#替换默认编码？

datanames = os.listdir('.\译文')

for dataname in datanames:
    if os.path.splitext(dataname)[1] == '.json':#遍历译文文件夹，筛选出译文json
        #找到json和对应的脚本
        yiwenjsonpath='.\译文\\'+dataname
        jiaobenpath='.\OriginFile\\rld\\'+dataname.replace('.json','.rld')
        outpath='.\\ChaosRegion_CHS\\rld\\'+dataname.replace('.json','.rld')

        #打开脚本和译文文件
        jiaoben=open(jiaobenpath, 'rb')
        jiaoben=jiaoben.read()
        yiwenjson=open(yiwenjsonpath, 'r',encoding='utf8')
        yiwenjson=json.load(yiwenjson)
        out=open(outpath, 'wb')

        #处理译文json成字典： "index"："post_zh_preview","name"
        yiwendic={}

        for dic in yiwenjson:
            #对译文的字符要进行处理，引用之前项目中的替换方法
            yiwendic[dic["index"]]=(wenbenchuli(dic["post_zh_preview"]),dic["name"])

        #按顺序匹配和替换原文
        search_pattern = bytes([0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0xFF,0x00, 0x00, 0x00, 0x00, 0x96, 0x00, 0x00, 0x00])
        start = 0
        i=0#用于匹配译文的序号
        #开始循环
        while True:
            start = jiaoben.find(search_pattern, start)
            if start == -1:
                break
            i+=1
            
            try:
                if "Failed translation" in yiwendic[i][0]:
                    raise RuntimeError
                bmessage=yiwendic[i][0].encode(encoding=outencode,errors='ignore')#将译文转化为二进制编码；
            except KeyError:
                print(dataname+' '+str(i)+' NOT FOUND')
                start += len(search_pattern)
                end = jiaoben.find(b'\x00', start)
                if end == -1:
                    break
                start = end + 1
                end = jiaoben.find(b'\x00', start)
                if end == -1:
                    break
                start = end + 1
                continue
            except RuntimeError:
                print(dataname+' '+str(i)+' Fail Trans')
                start += len(search_pattern)
                end = jiaoben.find(b'\x00', start)
                if end == -1:
                    break
                start = end + 1
                end = jiaoben.find(b'\x00', start)
                if end == -1:
                    break
                start = end + 1
                continue

            start += len(search_pattern)
            end = jiaoben.find(b'\x00', start)#这里为人名,之后可能会进行替换
            if end == -1:
                break
            
            #if True:#不替换名字
            if yiwendic[i][1]=='':
                bname_=b''
                start=end + 1
            else:
                if yiwendic[i][1] in namedict:
                    nametrans=hanzitihuan(namedict[yiwendic[i][1]])
                else:
                    nametrans=yiwendic[i][1]
                bname_=(nametrans+': ').encode(encoding=outencode,errors='ignore')
                bname=b'\x8b\x4c\x8f\x71'
                #bname=jiaoben[start:end].decode(encoding='sjis',errors='ignore').encode(encoding=outencode,errors='ignore')
                jiaoben=tihuan(jiaoben,start,end,bname)
                start = start + len(bname) + 1
            
            end = jiaoben.find(b'\x00', start)#这里的为文本
            if end == -1:
                break
            #进行替换：将[start:end]部分换为译文
            jiaoben=tihuan(jiaoben,start,end,bname_+bmessage)
            start += len(bname_+bmessage)
        if zititihuan:#开启字体替换
            jiaoben=jiaoben.replace(bori_font,bchanged_font)

        
        #对脚本章节名进行转化
        #章节名开头标识：00 0C 00 00 01
        search_pattern_1 = bytes([0x00,0x0C,0x00,0x00,0x01])
        start = 0
        while True:
            start = jiaoben.find(search_pattern_1, start)
            if start == -1:
                break
            start += len(search_pattern_1)
            end = jiaoben.find(b'\x00', start)
            if end == -1:
                break
            jiaoben=tihuan(jiaoben,start,end,jiaoben[start:end].decode(encoding='sjis',errors='ignore').encode(encoding=outencode,errors='ignore'))
        
        out.write(jiaoben)
        out.close()
#测试用，复制到游戏目录
#os.system('copy>nul 2>nul  "D:\鋼炎のソレイユ_chs\\rld_chs\\*.rld" "D:\game\ChaosRegion\\rld\\"')
#将原文件放回游戏：copy "D:\鋼炎のソレイユ_chs\\OriginFile\\rld\\*.rld" "D:\game\ChaosRegion\\rld\\"

'''
#对defchara进行处理
defcharapath='.\OriginFile\\rld\defChara.rld'
defcharaoutpath='.\\rld_chs\\defChara.rld'

defchar=open(defcharapath,'rb')
defchar=defchar.read()
defcharout=open(defcharaoutpath,'wb')

search_pattern = bytes([0x30,0x00,0x00,0x01])
start = 0
while True:
    start = defchar.find(search_pattern, start)
    if start == -1:
        break
    start += len(search_pattern)
    end = defchar.find(b'\x00', start)
    if end == -1:
        break
    defchar=defchar.replace(defchar[start:end],defchar[start:end].decode(encoding='sjis').encode(encoding='gbk'))
defcharout.write(defchar)
os.system('copy "D:\鋼炎のソレイユ_chs\\rld_chs\\defChara.rld" "D:\game\ChaosRegion\\rld\\"')
'''

os.system('copy README.md ChaosRegion_CHS\\')
os.system('del ChaosRegion_CHS.rar')
os.system('Rar a  -r -m2 ChaosRegion_CHS.rar ChaosRegion_CHS\\*')
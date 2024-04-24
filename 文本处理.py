from hanzidict import hanzidict

def hanzitihuan(text):#按照字典替换不支持的汉字，后续通过UniversalInjectorFramework替换回去以正常显示
    replaced_string=''
    for char in text:
        replaced_string += hanzidict.get(char, char)
    return replaced_string

def fuhaotihuan(text):#替换掉译文中一些不支持的常见特殊符号形式，以正常显示
    return text.replace('—','ー').replace('～','〜').replace('“','「').replace('”','」').replace('·','・')

def wenbenchuli(text):
    return fuhaotihuan(hanzitihuan(text))
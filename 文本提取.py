#存在很多问题，废弃
import re
def encode_shiftjis(input_bytes):
    encoded_bytes = b""
    error_encountered = False  # 用于跟踪是否遇到非法编码
    i = 0

    while i < len(input_bytes):
        try:
            current_byte = input_bytes[i]
            # 检查是否是ASCII控制字符（不包括可以显示的如换行符）
            if current_byte < 0x20 and current_byte not in (0x09, 0x0A, 0x0D):
                raise UnicodeDecodeError("shift_jis", b"", i, i+1, "Control character")
            # 检查半角假名
            if  (0xA1 <= current_byte <= 0xDF):
                #(0x20 <= current_byte <= 0x7E) or
                raise UnicodeDecodeError("shift_jis", b"", i, i+1, "Invalid half-width character")

            # 尝试将当前字节及可能的下一个字节一起解码再编码
            if (i + 1 < len(input_bytes)) and (0x81 <= current_byte <= 0x9F or 0xE0 <= current_byte <= 0xFC):
                # 可能是全角字符，包括当前字节和下一个字节
                test_bytes = input_bytes[i:i+2]
                test_bytes.decode('shift_jis')
                encoded_bytes += test_bytes
                i += 2  # 移动到下一个可能的字符开始
            else:
                # 只处理一个字节
                test_bytes = input_bytes[i:i+1]
                test_bytes.decode('shift_jis')
                encoded_bytes += test_bytes
                i += 1
            error_encountered = False  # 成功编码后，重置错误标志
        except UnicodeDecodeError:
            # 当遇到非法编码时，只有在之前没有遇到错误时才添加换行符
            if not error_encountered:
                encoded_bytes += b'\n'
                error_encountered = True  # 设置错误标志，避免连续添加换行符
            i += 1  # 移动到下一个字节继续尝试

    return encoded_bytes

def shaixuan(text):#进行筛选，去除掉非文本行。结合特点进行修改。
    text=text.replace(' ','').replace('\t','')
    if not re.search('[0-9,?@!\"]',text):
        if text !='\n':
            if len(text)>2 or (re.match('[\u4E00-\u9FFF\u3400-\u4DBF]',text)):
                if 'DLR' not in text:
                    if 'cmd' not in text:
                        if re.search('[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF…]',text):
                            return True
        

def read_binary_file_and_encode(path):
    # 从二进制文件中读取数据
    with open(path, 'rb') as file:
        content = file.read()

    # 编码数据
    encoded_bytes = encode_shiftjis(content)

    outpath=path.replace('.rld','')
    outpath_p=path.replace('.rld','.txt')
    # 将字节数据转换为字符串
    with open(outpath, 'w',encoding='utf8') as file:
        file.write(encoded_bytes.decode('shiftjis'))
    with open(outpath, 'r',encoding='utf8') as file:
        with open(outpath_p, 'w',encoding='utf8') as file_p:
            for line in file.readlines():
                if shaixuan(line):
                    file_p.write(line)
    return encoded_bytes.decode('shiftjis')  

import os

datanames = os.listdir('.\OriginFile\\rld')
for dataname in datanames:
    if os.path.splitext(dataname)[1] == '.rld':
        read_binary_file_and_encode('.\OriginFile\\rld\\'+dataname)
# -*- coding:utf-8 -*-
import struct
def test():
    str = '5A07A10100195B'
    str1 = ""  # 初始化
    str2 = ""  # 初始化
    while str:
        str1 = str[0:2]  # 分割字符串，获取前两个字符
        s = int(str1, 16)  # 字符串转换成16进制
        str2 += struct.pack('B', s)  # 转换成字节流，“B“为格式符，代表一个unsigned char （具体请查阅struct）
        str = str[2:]

    for data in str2:
        da= struct.unpack('B',data)
        print da[0]
        print int(hex(da[0]),16)
        print hex(da[0])



if __name__ == '__main__':
    test()
# -*- coding:utf-8 -*-
import redis
import struct
import time
from socket import *

from dal.infrastructure.bishuiyuan import BiShuiYuan

from common.createredis import create_redis,send_data


def SocketServer():
    try:
        dic = {}
        Colon = ServerUrl.find(':')
        IP = ServerUrl[0:Colon]
        Port = int(ServerUrl[Colon+1:])

        #建立socket对象
        print 'Server start:%s'%ServerUrl
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.setsockopt(SOL_SOCKET,SO_REUSEADDR, 1)

        #绑定IP端口号
        sockobj.bind((IP, Port))
        #监听，允许5个连结
        sockobj.listen(5)

        #直到进程结束时才结束循环
        tmp="5A05B2005B"
        send_data(tmp)
        while True:
            #等待client连结
            connection, address = sockobj.accept( )
            print 'Server connected by client:', address
            str= ''
            while True:
                re = redis.StrictRedis(host="123.56.201.7", port=6379)
                da = re.get("send_date")
                print da
                if  da=="aa":
                    time.sleep(5)
                    str="5A05A1015B"
                    str1 = ""  # 初始化
                    str2 = ""  # 初始化
                    while str:
                        str1 = str[0:2]  # 分割字符串，获取前两个字符
                        s = int(str1, 16)  # 字符串转换成16进制
                        str2 += struct.pack('B', s)  # 转换成字节流，“B“为格式符，代表一个unsigned char （具体请查阅struct）
                        str = str[2:]  # 分割字符串，去掉字符串前两个字符
                    connection.send(str2)
                    print 'Send RES:%s\r\n' % str2
                    # 读取Client消息包内容
                    data = connection.recv(1024)
                    num = len(data)
                    if num == 7:
                        tds = struct.unpack('B', data[4])[0]
                        water = struct.unpack('B', data[5])[0]
                        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                        dic["tds"] = tds
                        dic["water"] = water
                        dic["create_time"] =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                        create_redis(dic)
                        print tds
                        print water
                        BiShuiYuan.create(
                            tds=tds,
                            water=water,
                            create_time=create_time
                        )
                        # 如果没有data，跳出循环
                        # if not data: break
                        # 发送回复至Client
                        # RES='200 OK'
                        # connection.send(RES)
                    print 'Receive MSG:%s' % data.strip()
                else:
                    str=da
                    print str
                    str1 = ""  # 初始化
                    str2 = ""  # 初始化
                    if str=="5A05B2015B":
                        while str:
                            str1 = str[0:2]  # 分割字符串，获取前两个字符
                            s = int(str1, 16)  # 字符串转换成16进制
                            str2 += struct.pack('B', s)  # 转换成字节流，“B“为格式符，代表一个unsigned char （具体请查阅struct）
                            str = str[2:]  # 分割字符串，去掉字符串前两个字符
                        connection.send(str2)
                        print 'Send RES:%s\r\n' % str2
                        re.set("send_date", "aa")
                    elif str=="5A05B2005B":
                        while str:
                            str1 = str[0:2]  # 分割字符串，获取前两个字符
                            s = int(str1, 16)  # 字符串转换成16进制
                            str2 += struct.pack('B', s)  # 转换成字节流，“B“为格式符，代表一个unsigned char （具体请查阅struct）
                            str = str[2:]  # 分割字符串，去掉字符串前两个字符
                        connection.send(str2)
                        print 'Send RES:%s\r\n' % str2
                        dic["tds"] = ""
                        dic["water"] = ""
                        dic["create_time"] =""
                        create_redis(dic)
               #break
            #关闭Socket
            connection.close( )
    except Exception,ex:
        print ex

ServerUrl = "123.56.201.7:5678"
SocketServer()

#!/usr/bin/python3
# -*- coding:UTF-8 -*-
from socket import *  
from time import ctime  
  
HOST = ''  
PORT = 8888  
BUFSIZ = 128  
ADDR = (HOST, PORT)  
  
#创建一个服务器端UDP套接字  
udpServer = socket(AF_INET, SOCK_DGRAM)  
#绑定服务器套接字  
udpServer.bind(ADDR)  
  
while True:  
    print 'waiting for message...'  
#接收来自客户端的数据  
    data, addr = udpServer.recvfrom(BUFSIZ)  
    print 'get msg:',data
#向客户端发送数据  
    udpServer.sendto('[%s] %s' % (ctime(), data), addr)  
    print '...received from and returned to:', addr  
udpServer.close()  

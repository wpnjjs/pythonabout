# coding:utf-8

'''
@author: monster
@file: clienttcp.py
@time: 2018/1/20 上午10:36
'''

import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# 创建一个套接字（SOCK_STREAM:TCP套接字）
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # 连接服务器并发送数据
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")
    
    # 接受服务返回
    received = sock.recv(1024)
finally:
    sock.close()

print "Sent: {}".format(data)
print "Received:{}".format(received)

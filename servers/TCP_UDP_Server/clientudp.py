# coding:utf-8

'''
@author: monster
@file: clientudp.py
@time: 2018/1/20 下午12:12
'''

import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# UDP无连接，数据直接通过sendto发送给接受者
sock.sendto(data + "\n", (HOST, PORT))
received = sock.recv(1024)

print "SEND:{}".format(data)
print "RECEIVED:{}".format(received)

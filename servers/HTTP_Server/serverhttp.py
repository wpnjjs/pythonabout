# coding:utf-8

'''
@author: monster
@file: serverhttp.py
@time: 2018/1/22 上午10:12
'''

"""
    定义两个类（HTTPServer）实现HTTP服务。通常不直接使用，作为实现WebServer基础。以此为基础的类有（SimpleHTTPServer/CGIHTTPServer）
    
    HTTPServer
    继承 SockerServer.TCPServer, 并实现SockerServer.BaseServer的接口。创建并监听http套接字，分发请求到处理器。
    
    
    
"""

import SocketServer
import SimpleHTTPServer

class ThreadHTTPServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    pass

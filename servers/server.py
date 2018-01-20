# coding:utf-8

'''
@author: monster
@file: server.py
@time: 2018/1/19 下午7:39


Server，SocketServer a framework for network servers
extend relationship
BaseServer > TCPServer > UDPServer
TCPServer > UnixStreamServer 只适合Unix类型的平台使用
UDPServer > UnixDatagramServer 只适合Unix类型的平台使用

所有的都市队列形成处理请求，存在阻塞等待情况。使用多进程和多线程处理实现异步处理。使用ForkingMixIn and ThreadingMixIn混合类进行处理

创建一个服务的几步
1.创建一个请求处理类通过继承BaseRequestHandler类并且重新handler方法，此类处理传入的请求
2.实例化服务类，传递服务地址和请求处理的类（1中创建的类）。调用服务类实例的handler_request方法或者serve_forever方法来处理请求
3.调用服务类实例的server_close方法关闭socket
'''

import SocketServer


# TCPSERVER

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    服务器请求处理类
    每次连接到服务实例一次。必须重新handler方法实现和客户端的交互
    """
    
    def handle(self):
        # self.request 是被客户端连接TCP套接字，通过此对象获取客户端数据
        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data
        # 通过sendall返回请求的数据到客户端
        self.request.sendall(self.data.upper())


class MyTCPHandlerFileObject(SocketServer.StreamRequestHandler):
    """
    另一种请求处理类，使用流，通过提供文件对象的处理接口简化通信
    """
    
    def handle(self):
        # self.rfile 由handler创建的类文件对象，使用readline方法代替recv方法。readline方法中使用recv,会多次调用处理。直到遇到新行出现
        self.data = self.rfile.readline().strip()
        print "{} wrote:".format(self.client_address)
        print self.data
        # 同样，self.wfile 是类文件对象返回数据给客户端
        self.wfile.write(self.data.upper())


# UDPSERVER
class MyUDPHandler(SocketServer.BaseRequestHandler):
    """
    类似TCP，self.request是数据和socket成对组成。通过sendto返回数据给定客户端地址
    """
    
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print "{} wrote:".format(self.client_address[0])
        print data
        socket.sendto(data.upper(), self.client_address)


class MyUDPHandlerFileObject(SocketServer.DatagramRequestHandler):
    pass


if __name__ == "__main__":
    # TCPSERVER
    HOST, PORT = "localhost", 9999
    
    # 创建服务，绑定到本地9999端口
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    
    # 激活服务，此服务一直运行直到执行CTRL—C操作
    server.serve_forever()
    
    # UDPSERVER
    serverudp = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    serverudp.serve_forever()

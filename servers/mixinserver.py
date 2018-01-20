# coding:utf-8

'''
@author: monster
@file: mixinserver.py
@time: 2018/1/20 下午12:21
'''
import SocketServer
import threading
import socket


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{}: {}".format(cur_thread.name, data)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def client(ip, port, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(data)
        resp = sock.recv(1024)
        print "Received:{}".format(resp)
    finally:
        sock.close()


if __name__ == "__main__":
    # 端口给0，选择一个未使用的端口
    HOST, PORT = "localhost", 0
    
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    
    print ip, port
    # 通过线程启动此服务，此线程将为每一个请求创建一个或多个线程进行请求处理
    server_thread = threading.Thread(target=server.serve_forever)
    # 退出服务进程在主线程终结
    server_thread.setDaemon(True)
    server_thread.start()
    
    print "服务循环运行使用的线程", server_thread.name
    
    client(ip, port, "a")
    client(ip, port, "b")
    client(ip, port, "c")
    
    server.shutdown()
    server.server_close()

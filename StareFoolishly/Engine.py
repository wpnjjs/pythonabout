# coding:utf-8

'''
@author: monster
@file: Engine.py
@time: 2018/2/1 下午3:49
'''


import GameFactory


class A(object):
    def __init__(self):
        self.a = "A class"
    
    def parsemsg(self, msg, callback):
        print msg + "A"
        rst = msg + " back"
        print type(A)
        callback(rst)


config = {"1": GameFactory(A)}


class Engine:
    def __init__(self):
        pass
    
    def doloop(self, msg, callback):
        print msg
        config[msg[0]].parsemsg(msg, callback)


def up(msg, callback, resp):
    callback(msg, resp)


def down(msg):
    print msg


if __name__ == '__main__':
    engine = Engine()
    up("1", engine.doloop, down)

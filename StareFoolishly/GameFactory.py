# coding:utf-8

'''
@author: monster
@file: GameFactory.py
@time: 2018/2/1 下午7:05
'''


class GameFactory(object):
    def __init__(self, cls):
        self.gameo = cls
        self.backcall = lambda x: x
    
    def parsemsg(self, msg, callback):
        self.backcall = callback
        self.gameo.parsemsg(msg, self.backmsg)
    
    def backmsg(self, backmsg):
        print backmsg
        self.backcall(backmsg)

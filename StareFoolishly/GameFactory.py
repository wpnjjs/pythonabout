# coding:utf-8

'''
@author: monster
@file: GameFactory.py
@time: 2018/2/1 下午7:05
'''


class GameFactory(object):
    def __init__(self, cls, db):
        self.gameo = cls
        self.backcall = lambda x: x
    
    def parsemsg(self, msg, callback):
        self.backcall = callback
        gameobj = self.gameo()
        gameobj.parsemsg(msg, self.backmsg)
    
    def backmsg(self, backmsg):
        print backmsg
        self.backcall(backmsg)

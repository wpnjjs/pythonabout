# coding:utf-8

'''
@author: monster
@file: Home.py
@time: 2018/2/1 下午7:07
'''


class Room:
    def __init__(self):
        pass
    
    def getroomid(self):
        return _roomidlist.pop(0)
    
    def releaseroomid(self, roomid):
        _roomidlist.append(roomid)
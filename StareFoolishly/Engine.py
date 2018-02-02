# coding:utf-8

"""
@author: monster
@file: Engine.py
@time: 2018/2/1 下午3:49
"""

from GameFactory import GameFactory
from StareFoolishly import StareFoolishly
import Util

redis_config = Util.dict_to_object({
    'host': 'localhost',
    'port': 6379,
})

game_map = {"1": GameFactory(StareFoolishly, 0)}


class Engine:
    def __init__(self):
        pass
    
    def do_loop(self, msg, callback):
        game_map[msg[0]].parsemsg(msg, callback)


def up(msg, callback, resp):
    callback(msg, resp)


def down(msg):
    print msg


if __name__ == '__main__':
    engine = Engine()
    up("1", engine.do_loop, down)

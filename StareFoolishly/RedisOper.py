# coding:utf-8

'''
@author: monster
@file: RedisOper.py
@time: 2018/2/1 下午7:23
'''

import redis


class RedisOper(object):
    def __init__(self):
        self.pool = redis.Connection(host='localhost', port=6379, db=0)
        self.redishandle = redis.Redis(connection_pool=self.pool, )
        
        # def set

# coding:utf-8

'''
@author: monster
@file: Util.py
@time: 2018/2/1 下午5:29
'''

import math


class Util:
    def __init__(self):
        pass
    
    @staticmethod
    def _zuhe(seed=10, n=1):
        '''
        获取seed的全部有序组合情况。
        :param seed: 种子列表
        :param n: 位数
        :return: 有序的所有组合列表
        '''
        seed = seed if isinstance(seed, list) else [str(i) for i in range(seed)]
        
        keys = []
        
        for i in range(int(math.pow(len(seed), n))):
            genkey = '0' * (n - len(str(i))) + str(i)
            
            keys.append(genkey)
        
        return keys


def dict_to_object(dict_object):
    top = type('new', (object,), dict_object)
    
    seqs = tuple, list, set, frozenset
    
    for key, value in dict_object.items():
        
        if isinstance(value, dict):
            
            setattr(top, key, dict_to_object(value))
        
        elif isinstance(value, seqs):
            
            setattr(top, key, type(value)(dict_to_object(v) if isinstance(v, dict) else v for v in value))
        
        else:
            
            setattr(top, key, value)
    
    return top

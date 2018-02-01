# coding:utf-8

'''
@author: monster
@file: dot.py
@time: 2018/2/1 上午11:02
'''

import math


def zuhe(seed=10, n=1):
    
    seed = seed if isinstance(seed, list) else [str(i) for i in range(seed)]
    
    keys = []
    
    for i in range(int(math.pow(len(seed), n))):
        genkey = '0' * (n - len(str(i))) + str(i)
        
        keys.append(genkey)
    
    return keys


res = zuhe(n=2)
print res, len(res)
# coding:utf-8

"""
@author: monster
@file: dicttoobj.py
@time: 2018/2/2 下午1:52
"""


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

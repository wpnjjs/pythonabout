# coding:utf-8

'''
@author: monster
@file: objectserializeutils.py
@time: 2018/1/18 下午6:42
'''

import pickle
import json


class SerializeObject(object):
    @staticmethod
    def serialize(clsobj, serializetype='pickle'):
        '''
        将对象序列化，pickle模块序列化或json模块序列化
        :param clsobj: 需要序列化的对象
        :param serializetype: 序列化类型，pickle，使用pickle方式序列化；json，使用json方式序列化
        :return: 序列化结果
        '''
        
        switch = {
            "pickle": lambda obj: pickle.dumps(obj),
            "json": lambda obj: json.dumps(obj.__dict__)
        }
        
        try:
            return switch[serializetype](clsobj)
        except KeyError as e:
            raise e
    
    @staticmethod
    def unserialize(datastr, serializetype='pickle'):
        '''
        反序列化
        :param datastr: 序列化字符串
        :param serializetype: 何种方式反序列化，一定要对应
        :return: 反序列化结果，pickle方式反序列化为对应类型，json方式返回字典对象，需要自己变为对应的对象
        '''
        
        switch = {
            "pickle": lambda s: pickle.loads(s),
            "json": lambda s: json.loads(s)
        }
        
        try:
            return switch[serializetype](datastr)
        except KeyError as e:
            raise e


if __name__ == '__main__':
    '''
    eg.
    '''
    
    
    class TObj(object):
        def __init__(self):
            self._a = 1
        
        @property
        def a(self):
            print self._a
    
    
    a = TObj()
    bytedata = SerializeObject.serialize(a)
    print bytedata, a.__dict__
    print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<"
    b = SerializeObject.unserialize(bytedata)
    b.a
    
    jsonsdata = SerializeObject.serialize(b, serializetype='json')
    print jsonsdata
    print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<"
    c = SerializeObject.unserialize(jsonsdata, serializetype='json')
    print c

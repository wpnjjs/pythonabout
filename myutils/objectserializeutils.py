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
        ''''''
        
        def pickleserialize(clsobjpickle):
            return pickle.dumps(clsobjpickle)
        
        def jsonserialize(clsobjjson):
            print clsobjjson.__dict
            return json.dumps(clsobjjson.__dict)
        
        switch = {
            "pickle": pickleserialize,
            "json": jsonserialize
        }
        
        try:
            return switch[serializetype](clsobj)
        except KeyError as e:
            raise e
    
    @staticmethod
    def unserialize(serializetype='pickle'):
        pass


class TObj(object):
    def __init__(self):
        self._a = 1
    
    @property
    def a(self):
        print self._a


if __name__ == '__main__':
    import pickle
    
    a = TObj()
    # bytedata = pickle.dumps(a)
    bytedata = SerializeObject.serialize(a)
    print bytedata
    print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<"
    b = pickle.loads(bytedata)
    b.a
    
    jsonsdata = SerializeObject.serialize(a, serializetype='json')
    print jsonsdata
    print ">>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<"
    c = json.loads(jsonsdata)
    c.a
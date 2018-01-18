# coding:utf-8

'''
@author: monster
@file: enumvarious.py
@time: 2018/1/18 下午7:00
'''


# 新版Python用户（Python 3.4 with PEP 435)

# from enum import Enum
# Animal = Enum('A','B')
# or
# class Animal(Enum):
#     a = 1
#     b = 2

def enum(**enums):
    '''
    老版本python实现enum类型
    :param enums: 枚举元素
    :return: 返回对应枚举元素
    
    class type(name, bases, dict)
        With three arguments, return a new type object. This is essentially a dynamic form of the class statement.
        The name string is the class name and becomes the name attribute; the bases tuple itemizes the base classes
        and becomes the bases attribute; and the dict dictionary is the namespace containing definitions for class
        body and becomes the dict attribute. For example, the following two statements create identical type objects:
        
    eg.
    Number = enum(ONE=1, TWO=2)
    print Number.ONE
    '''
    return type('Enum', (), enums)


if __name__ == '__main__':
    pass

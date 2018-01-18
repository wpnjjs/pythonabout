# coding:utf-8

'''
@author: monster
@file: modifier.py
@time: 2018/1/15 下午12:46
'''


def modifier(f):
    print "before", f, type(f)
    f()
    print "after"


def modifier1(f):
    print "before1"
    
    def add2():
        print f() + 1
    
    return add2
    print "after1"


@modifier
@modifier1
def add():
    return 1 + 1

#
# def modifier1(parameter):
#     print "outter function transfer parameter is >", parameter
#
#     def warpin(func):
#         print "inner function do before"
#         func()
#         print "inner function do after"

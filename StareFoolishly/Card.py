# coding:utf-8

'''
@author: monster
@file: Card.py
@time: 2018/2/1 下午7:04
'''

import random


class Card(object):
    def __init__(self, jokerneed=True, pairs=1):
        self.number = 54 * pairs
        self.pairs = pairs
        self.suits = ['r', 'b', 's', 'd', 'j']
        self.jokerslist = ['j0', 'j1']
        self.cardslist = [
            'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'ra', 'rb', 'rc', 'rd', 're',
            'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be',
            's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'sa', 'sb', 'sc', 'sd', 'se',
            'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de',
        ]
        self.cardslist.extend(self.jokerslist) if jokerneed else self.cardslist
        self.cardslist *= pairs
    
    def deal(self, cardnumber):
        print "cardnumber", cardnumber
        number = cardnumber
        dealcards = []
        while number != 0:
            dealcards.append(self.cardslist.pop(0))
            number -= 1
        else:
            return dealcards
    
    def shufflecard(self):
        random.shuffle(self.cardslist)
        random.shuffle(self.cardslist)
    
    def getleavecards(self):
        return self.cardslist
    
    def getleavecardsNO(self):
        return len(self.cardslist)

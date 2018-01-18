# coding:utf-8

'''
@author: monster
@file: StareFoolishly.py
@time: 2018/1/5 下午1:15
'''

import random


class Card(object):
    def __init__(self, number=54, pairs=1):
        self.number = number
        self.pairs = pairs
        self.suits = ['r', 'b', 's', 'd', 'c']
        self.cardslist = [
            're', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'ra', 'rb', 'rc', 'rd',
            'be', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd',
            'se', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 'sa', 'sb', 'sc', 'sd',
            'de', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd',
        
        ]
    
    #     'c0', 'c1',
    
    def deal(self, cardnumber):
        print "cardnumber", cardnumber
        self.shufflecard()
        number = cardnumber
        dealcards = []
        while number != 0:
            dealcards.append(self.cardslist.pop(0))
            number -= 1
        else:
            return dealcards
    
    def shufflecard(self):
        random.shuffle(self.cardslist)
    
    def getleavecards(self):
        return self.cardslist


class StareFoolishly(object):
    def __init__(self):
        self.cardpriority = "3456789abcde2"
        self.joker = 'c'
        self.cardstype = {"sola": 0,  # 单张
                          "pair": 1,  # 对子
                          # "straight_pair": 2,  # 对子
                          "straight": 2,  # 顺子
                          "bomb": 3,  # 炸弹
                          }
    
    def check_cards_type(self, cards):
        if len(cards) == 1:
            return
        if len(cards) == 2 and True:
            pass
    
    def tips_put(self, cardsinhand, putcards=None):
        exceptjoker = [c for c in cardsinhand if c[0] != 'c']
        numlistofexceptjoker = [n[1] for n in exceptjoker]
        setnumstrofcards = ''.join(sorted(list(set(numlistofexceptjoker))))
        if putcards:
            pass
        else:
            lenofinhandlist = len(cardsinhand)
            lenofinhandset = len(set(cardsinhand))
    
    def getstraight(self, cards):
        '''
        分析手牌中顺子
        :param cards: 手牌
        :return: 返回顺子的列表
        '''
        noofcards = [c[1] for c in cards]
        noofcardsexceptjokers = [n for n in noofcards if n not in ['0', '1']]
        jokerno = [n for n in noofcards if n in ['0', '1']]
        strofcardno = ''.join(sorted(list(set(noofcardsexceptjokers))))
        straightstr = "e23456789abcde"
        lenght = len(strofcardno)
        checkstraightlist = []
        print "lenght>>", lenght
        if lenght > 2:
            for a in range(3, lenght + 1):
                for b in range(a - 2):
                    strlen = lenght - (a - 3)
                    print "strofcardno[b:b + strlen]", strofcardno[b:b + strlen]
                    if strofcardno[b:b + strlen] in straightstr:
                        checkstraightlist.append(strofcardno[b:b + strlen])
                    else:
                        continue
        if (lenght + len(jokerno)) > 2 and len(jokerno) > 0:
            listofcardno = list(strofcardno)
            listofcardno = sorted(listofcardno, reverse=True)
            print "listofcardno", listofcardno
            dengchalist = [int(listofcardno[i], 16) - int(listofcardno[i + 1], 16) for i in
                           range(len(listofcardno) - 1)]
            exchange = [hex(cha)[-1] if cha > 9 else cha for cha in dengchalist]
            exchange.reverse()
            print "exchange", exchange
            if exchange:
                if len(set(exchange)) == 1 and 1 in set(exchange):
                    checkstraightlist.append(strofcardno + ''.join(jokerno))
                strdigui = reduce(lambda x, y: '%s%s' % (x, y), exchange)
                strdigui = str(strdigui) if len(exchange) == 1 else strdigui
                print "strdigui", strdigui
                lenghtdigui = len(strdigui)
                if len(jokerno):
                    for h in range(1, lenghtdigui + 1):
                        for i in range(h):
                            strlen = lenghtdigui + 1 - h
                            print "strlen 1jokers >>", strlen, strdigui[i:i + strlen]
                            if set(list(strdigui[i:i + strlen])) == set(['1', ]):
                                checkstraightlist.append(strofcardno[i:(i + 1 + strlen)] + jokerno[0])
                            case1 = (strdigui[i:i + strlen] in ['1', '2'])
                            case2 = (
                                strdigui[i:i + strlen].count('2') == 1 and set(list(strdigui[i:i + strlen])) == set(
                                        ['1',
                                         '2']))
                            if case1 or case2:
                                print "strofcardno[(i + 1):(i + 1 + strlen)]", strofcardno[(i + 1):(i + 1 + strlen)]
                                checkstraightlist.append(strofcardno[i:(i + 1 + strlen)] + jokerno[0])
                elif len(jokerno) == 2:
                    for h in range(1, lenghtdigui + 1):
                        for i in range(h):
                            strlen = lenghtdigui + 1 - h
                            print "strlen 2jokers >>", strlen, strdigui[i:i + strlen]
                            if set(list(strdigui[i:i + strlen])) == set(['1', ]):
                                checkstraightlist.append(strofcardno[i:(i + 1 + strlen)] + ''.join(jokerno))
                            case0 = (strdigui[i:i + strlen] in ['1', '2', '3'])
                            case1 = (
                                strdigui[i:i + strlen].count('3') == 1 and set(list(strdigui[i:i + strlen])) == set(
                                        ['1',
                                         '3']))
                            case2 = (
                                strdigui[i:i + strlen].count('2') == 2 and set(list(strdigui[i:i + strlen])) == set(
                                        ['1',
                                         '2']))
                            if case0 or case1 or case2:
                                checkstraightlist.append(strofcardno[i:(i + 1 + strlen)] + ''.join(jokerno))
            else:
                checkstraightlist.append(strofcardno + ''.join(jokerno))
        print "getstraight>>************************************************************************", checkstraightlist
        result = sorted(list(set(checkstraightlist)), key=lambda x: len(x), reverse=True)
        print "result>>************************************************************************", result
        return result
    
    def getbomb(self, cards):
        '''
        分析手牌中的炸弹
        :param cards: 手牌
        :return: 返回炸弹列表
        '''
        noofcards = [c[1] for c in cards]
        noofcardsexceptjokers = [n for n in noofcards if n not in ['0', '1']]
        jokerno = [n for n in noofcards if n in ['0', '1']]
        strofcardno = ''.join(sorted(list(set(noofcardsexceptjokers))))
        bombanalysisresult = []
        for i in range(len(strofcardno)):
            if noofcards.count(strofcardno[i]) > 2:
                bombanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]))
        if len(jokerno):
            for ii in range(len(strofcardno)):
                if noofcards.count(strofcardno[i]) > 1:
                    bombanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]) + jokerno[0])
        elif len(jokerno) == 2:
            for ii in range(len(strofcardno)):
                if noofcards.count(strofcardno[i]) > 0:
                    bombanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]) + ''.join(jokerno))
        result = sorted(list(set(bombanalysisresult)), key=lambda x: len(x), reverse=True)
        return result
    
    def getpairs(self, cards):
        '''
        分析对子
        :param cards: 手牌
        :return: 对子列表
        '''
        noofcards = [c[1] for c in cards]
        noofcardsexceptjokers = [n for n in noofcards if n not in ['0', '1']]
        jokerno = [n for n in noofcards if n in ['0', '1']]
        strofcardno = ''.join(sorted(list(set(noofcardsexceptjokers))))
        pairsanalysisresult = []
        for i in range(len(strofcardno)):
            if noofcards.count(strofcardno[i]) == 2:
                pairsanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]))
        if len(jokerno):
            for ii in range(len(strofcardno)):
                if noofcards.count(strofcardno[i]) == 1:
                    pairsanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]) + jokerno[0])
        result = sorted(list(set(pairsanalysisresult)), key=lambda x: len(x), reverse=True)
        return result
    
    def checkputcardstypeandnext(self, cards):
        '''
        检查出牌类型，给出接牌和其他相关牌型
        :param cards: 出牌
        :return: 出牌类型
        self.cardstype = {"sola": 0,  # 单张
                  "pair": 1,  # 对子
                  # "straight_pair": 2,  # 对子
                  "straight": 2,  # 顺子
                  "bomb": 3,  # 炸弹
                  }
        '''
        noofcards = [c[1] for c in cards]
        noofcardsexceptjokers = [n for n in noofcards if n not in ['0', '1']]
        jokerno = [n for n in noofcards if n in ['0', '1']]
        strofcardno = ''.join(sorted(list(set(noofcardsexceptjokers))))
        nextput = []
        lenght = len(cards)
        if lenght == 1:
            if self.cardpriority.index(noofcards[0]) + 1 != len(self.cardpriority):
                nextput.extend([self.cardpriority[self.cardpriority.index(noofcards[0]) + 1], '2'])
            nextput = list(set(nextput))
            nextput = sorted(nextput, key=lambda x: self.cardpriority.index(x))
            nextput.append('bomb')
            return [self.cardstype["sola"], nextput]
        if lenght == 2:
            if self.cardpriority.index(noofcardsexceptjokers[0]) + 1 != len(self.cardpriority):
                nextput.extend([self.cardpriority[self.cardpriority.index(noofcardsexceptjokers[0]) + 1] * 2, '22'])
            nextput = list(set(nextput))
            nextput = sorted(nextput, key=lambda x: self.cardpriority.index(x[0]))
            nextput.append('bomb')
            return [self.cardstype["pair"], nextput]
        if lenght > 2:
            if len(set(noofcardsexceptjokers)) == 1:
                nextput.append('bomb')
                return [self.cardstype["bomb"], [lenght, noofcardsexceptjokers[0]]]
            else:
                # mincno = min(noofcardsexceptjokers)
                maxcno = max(noofcardsexceptjokers)
                lenjoker = len(jokerno)
                if lenjoker > 0:
                    listofcardno = list(strofcardno)
                    listofcardno = sorted(listofcardno, reverse=True)
                    print "listofcardno", listofcardno
                    dengchalist = [int(listofcardno[i], 16) - int(listofcardno[i + 1], 16) for i in
                                   range(len(listofcardno) - 1)]
                    exchange = [hex(cha)[-1] if cha > 9 else str(cha) for cha in dengchalist]
                    exchange.reverse()
                    print "exchange", exchange
                    if exchange:
                        if lenjoker == 1:
                            maxcno = maxcno if exchange.count('2') == 1 else (
                                maxcno if maxcno == 'e' else self.cardpriority[self.cardpriority.index(maxcno) + 1])
                            if maxcno != 'e':
                                indexofmax = self.cardpriority.index(maxcno)
                                nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                        else:
                            case1 = exchange.count('2') == 0 and exchange.count('3') == 0
                            if case1 and self.cardpriority.index(maxcno) < self.cardpriority.index('e') - 2:
                                indexofmax = self.cardpriority.index(maxcno) + 2
                                nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                            case2 = exchange.count('2') == 1
                            if case2 and self.cardpriority.index(maxcno) < self.cardpriority.index('e') - 1:
                                indexofmax = self.cardpriority.index(maxcno) + 1
                                nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                            case3 = exchange.count('2') == 2
                            if case3:
                                if maxcno != 'e':
                                    indexofmax = self.cardpriority.index(maxcno)
                                    nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                            case4 = exchange.count('3') == 1
                            if case4:
                                if maxcno != 'e':
                                    indexofmax = self.cardpriority.index(maxcno)
                                    nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                    # never in this branch
                    # else:
                    #     indexofmax = self.cardpriority.index(mincno) + lenght
                    #     if self.cardpriority.index('e') >indexofmax:
                    #         nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                else:
                    finalno = maxcno
                if finalno != 'e':
                    indexofmax = self.cardpriority.index(finalno)
                    nextput.append(self.cardpriority[indexofmax - lenght + 2:indexofmax + 2])
                nextput.append('bomb')
                return [self.cardstype["straight"], nextput]
    
    def getnext(self, cards):
        pass


if __name__ == "__main__":
    for i in range(100):
        card = Card()
        cadeal = card.deal(random.randint(1, 6))
        print "deal cards", cadeal
        noofcards = [c[1] for c in cadeal]
        strnoofcards = ''.join(sorted(list(set(noofcards))))
        print "noofcards", noofcards, strnoofcards
        jokerlist = ['0', '1']
        jokerc = jokerlist[:random.randint(0, 2)]
        print "jokerc", jokerc
        # getstraight(strnoofcards, jokerc)

# coding:utf-8

'''
@author: monster
@file: StareFoolishly.py
@time: 2018/1/5 下午1:15
'''

import random, copy


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


class StareFoolishly(Card):
    def __init__(self):
        self.events = {"deal": 0, "get": 1, "put": 2, "pass": 3, "balance": 4}
        self.cardpriority = "3456789abcde201"  # 牌值大小
        self.joker = 'j'  # 癞子
        self.cardstype = {"sola": 0,  # 单张
                          "pair": 1,  # 对子
                          # "straight_pair": 2,  # 对子
                          "straight": 2,  # 顺子
                          "boom": 3,  # 炸弹
                          }  # 可出的牌型
        self.leftcards = []  # 剩余牌
        self.leftcardsno = 0  # 剩余排数
        self.deskno = ""  # 桌号
        self.playerno = 0  # 玩家个数
        self.winner = ""  # 赢家
        self.playerlist = [None, ] * 6  # 玩家列表
        self.gamingplayerlist = []  # 游戏中的玩家
        self.playermapcardsinhands = {}  # 玩家和手牌映射关系
        self.playermapputcards = {}  # 玩家和出牌映射关系
        self.playermapgetcards = {}  # 玩家和摸排映射关系
        self.trustshiplist = []  # 玩家托管列表
        self.outlinelist = []  # 玩家离线列表
        self.eventsrecord = []  # 事件记录[uid, event, cards, cardtype, message（可选）]
        self.currentplayer = ""  # 当前玩家
    
    def createdesk(self):
        number = list("0123456789") * 6
        idx = random.randint(0, 54)
        self.deskno = ''.join(number[idx:idx])
    
    def join(self):
        self.playerlist = ['1', '2', '3', '4', '5', '6']
        self.winner = '1'
    
    def dealcard(self):
        self.gamingplayerlist = copy.deepcopy(self.playerlist)
        card = Card()
        card.shufflecard()
        for p in self.gamingplayerlist:
            if p == self.winner:
                self.playermapcardsinhands.update(
                        {p: sorted(card.deal(6),
                                   key=lambda x: self.cardpriority.index(x[1]) + card.suits.index(x[0]) * 0.1,
                                   reverse=True)})
            else:
                self.playermapcardsinhands.update(
                        {p: sorted(card.deal(5),
                                   key=lambda x: self.cardpriority.index(x[1]) + card.suits.index(x[0]) * 0.1,
                                   reverse=True)})
        self.leftcards = card.getleavecards()
    
    def tips_put(self, putcards=None):
        tips = []
        result = None
        if putcards:
            result = self.checkputcardstypeandnext(putcards)
        self.getnext(result)
        tips
    
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
    
    def getboom(self, cards):
        '''
        分析手牌中的炸弹
        :param cards: 手牌
        :return: 返回炸弹列表
        '''
        noofcards = [c[1] for c in cards]
        noofcardsexceptjokers = [n for n in noofcards if n not in ['0', '1']]
        jokerno = [n for n in noofcards if n in ['0', '1']]
        strofcardno = ''.join(sorted(list(set(noofcardsexceptjokers))))
        boomanalysisresult = []
        for i in range(len(strofcardno)):
            if noofcards.count(strofcardno[i]) > 2:
                boomanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]))
        if len(jokerno):
            for ii in range(len(strofcardno)):
                if noofcards.count(strofcardno[i]) > 1:
                    boomanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]) + jokerno[0])
        elif len(jokerno) == 2:
            for ii in range(len(strofcardno)):
                if noofcards.count(strofcardno[i]) > 0:
                    boomanalysisresult.append(strofcardno[i] * noofcards.count(strofcardno[i]) + ''.join(jokerno))
        result = sorted(list(set(boomanalysisresult)), key=lambda x: len(x), reverse=True)
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
                  "boom": 3,  # 炸弹
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
            nextput.append('boom')
            return [self.cardstype["sola"], nextput]
        if lenght == 2:
            if self.cardpriority.index(noofcardsexceptjokers[0]) + 1 != len(self.cardpriority):
                nextput.extend([self.cardpriority[self.cardpriority.index(noofcardsexceptjokers[0]) + 1] * 2, '22'])
            nextput = list(set(nextput))
            nextput = sorted(nextput, key=lambda x: self.cardpriority.index(x[0]))
            nextput.append('boom')
            return [self.cardstype["pair"], nextput]
        if lenght > 2:
            if len(set(noofcardsexceptjokers)) == 1:
                nextput.append('boom')
                return [self.cardstype["boom"], [lenght, noofcardsexceptjokers[0]]]
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
                nextput.append('boom')
                return [self.cardstype["straight"], nextput]
    
    def getnext(self, rst):
        print rst
        if rst:
            pass
        else:
            if '3' in


class Control(object):
    pass


if __name__ == "__main__":
    import json, pickle
    
    s = StareFoolishly()
    s.createdesk()
    s.join()
    s.dealcard()
    datajson = json.dumps(s.__dict__)
    print datajson
    datapickle = pickle.dumps(s)
    ss = pickle.loads(datapickle)
    ss.dealcard()
    print json.dumps(ss.__dict__)
    ss.tips_put()

from os import sys
import argparse
parser = argparse.ArgumentParser(description='Argument Parser')
parser.add_argument('pp', type=int, help='Number of plat peices')
parser.add_argument('gp', type=int, help='Number of gold peices')
parser.add_argument('ep', type=int, help='Number of epsom peices')
parser.add_argument('sp', type=int, help='Number of silver peices')
parser.add_argument('cp', type=int, help='Number of copper peices')
parser.add_argument('numPlayers', type=int, help='Number of players')
parser.add_argument('--tengem', type=int, help='Number of gems @ 10g')
parser.add_argument('--fiftygem', type=int, help='Number of gems @ 50g')
parser.add_argument('--hundredgem', type=int, help='Number of gems @ 100g')
parser.add_argument('--fivegem', type=int, help='Number of gems @ 500g')

def findLowest(players,num):
    for x in players:
        if x.total() == num:
            return x
    print("couldnt find low value")

ppf = 0
gpf = 0
epf = 0
spf = 0
cpf = 0
ten = 0
fifty = 0
hundred = 0
five = 0

def main(pp,gp,ep,sp,cp,players,*args):
    global ppf
    global gpf
    global epf
    global spf
    global cpf
    global ten
    global fifty
    global hundred
    global five

    if args:
        if 'tengem' in args[0]:
            ten = args[0]['tengem']
        if 'fiftygem' in args[0]:
            fifty = args[0]['fiftygem']
        if 'hundredgem' in args[0]:
            hundred = args[0]['hundredgem']
        if 'fivegem' in args[0]:
            five = args[0]['fivegem']



    ppf = float(pp)
    gpf = float(gp)
    epf = float(ep)
    spf = float(sp)
    cpf = float(cp)
    playersf = int(players)
    total_gold = (ppf * 10) + gpf + (epf/2)+ (spf/10) + (cpf/100) + (ten * 10) + (fifty * 50) + (hundred * 100) + (five * 500)
    print('Total gold value: ' + str(total_gold))
    per_player = total_gold/playersf
    print(str(per_player) + ' Per person')

    class player(object):
        def __init__(self, name, pp, gp, ep, sp, cp, ten, fifty, hundred, five):
            self.pp = pp
            self.gp = gp
            self.ep = ep
            self.sp = sp
            self.cp = cp
            self.ten = ten
            self.fifty = fifty
            self.hundred = hundred
            self.five = five
            self.name = name
        def addP(self):
            self.pp += 1
            global ppf
            ppf = ppf - 1
        def addG(self):
            self.gp += 1
            global gpf
            gpf = gpf - 1
        def addE(self):
            self.ep += 1
            global epf
            epf = epf - 1
        def addS(self):
            self.sp += 1
            global spf
            spf = spf - 1
        def addC(self):
            self.cp += 1
            global cpf
            cpf =  cpf - 1
        def addTen(self):
            self.ten += 1
            global ten
            ten = ten - 1
        def addFifty(self):
            self.fifty += 1
            global fifty
            fifty = fifty - 1
        def addHundred(self):
            self.hundred += 1
            global hundred
            hundred = hundred - 1
        def addFive(self):
            self.five += 1
            global five
            five = five - 1
        def getDiff(self):
            res = self.total() - per_player
            return res
        def totalGems(self):
            res = (self.ten * 10) + (self.fifty * 50) + (self.hundred * 100) + (self.five * 500)
            return res
        def total(self):
            res = float((self.pp * 10) + (self.gp) + (self.ep/2) + (self.sp/10) + (self.cp * .001) + (self.ten * 10) + (self.fifty * 50) + (self.hundred * 100) + (self.five * 500))
            return res
        def makeMessage(self):
            message = self.name + ' recieves: ' + str(self.pp) + 'P, ' + str(self.gp) + 'G, ' + str(self.ep) + 'E, ' + str(self.sp) + 'S, ' + str(self.cp) + 'C, and ' + str(self.totalGems()) + ' worth of gems, ' + 'with a difference of ' + str(self.getDiff())
            return message

    player1 = player('player1',0,0,0,0,0,0,0,0,0)
    player2 = player('player2',0,0,0,0,0,0,0,0,0)
    player3 = player('player3',0,0,0,0,0,0,0,0,0)
    player4 = player('player4',0,0,0,0,0,0,0,0,0)
    player5 = player('player5',0,0,0,0,0,0,0,0,0)
    player6 = player('player6',0,0,0,0,0,0,0,0,0)
    player7 = player('player7',0,0,0,0,0,0,0,0,0)
    player8 = player('player8',0,0,0,0,0,0,0,0,0)

    player_pool = [player1,player2,player3,player4,player5,player6,player7,player8]
    player_pool = player_pool[0:playersf]

    while five > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addFive()
    while hundred > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addHundred()
    while fifty > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addFifty()
    while ten > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addTen()
    while ppf > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addP()
    while gpf > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addG()
    while epf > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addE()
    while spf > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addS()
    while cpf > 0:
        totals = []
        for i in range(0,len(player_pool)):
            totals.append(player_pool[i].total())
        low = min(totals)
        print(low)
        lowest_player = findLowest(player_pool,low)
        lowest_player.addC()
    for x in player_pool:
        print (x.makeMessage())

if __name__ == "__main__":
    args = parser.parse_args()
    options = {}
    if args.tengem is not None:
        options['tengem'] = args.tengem
    if args.fiftygem is not None:
        options['fiftygem'] = args.fiftygem
    if args.hundredgem is not None:
        options['hundredgem'] = args.hundredgem
    if args.fivegem is not None:
        options['fivegem'] = args.fivegem
    main(args.pp, args.gp, args.ep, args.sp, args.cp, args.numPlayers, options)

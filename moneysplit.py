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
    playersf = float(players)
    total_gold = (ppf * 10) + gpf + (epf/2)+ (spf/10) + (cpf/100) + (ten * 10) + (fifty * 50) + (hundred * 100) + (five * 500)
    print('Total gold value: ' + str(total_gold))
    per_player = total_gold/playersf
    print(str(per_player) + ' Per person')

    class player(object):
        def __init__(self, pp, gp, ep, sp, cp, ten, fifty, hundred, five):
            self.pp = pp
            self.gp = gp
            self.ep = ep
            self.sp = sp
            self.cp = cp
            self.ten = ten
            self.fifty = fifty
            self.hundred = hundred
            self.five = five
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
        def total(self):
            res = (self.pp * 10) + self.gp + (self.ep/2) + (self.sp/10) + (self.cp/100) + (self.ten * 10) + (self.fifty * 50) + (self.hundred * 100) + (self.five * 500)
            return res

    player1 = player(0,0,0,0,0,0,0,0,0)
    player2 = player(0,0,0,0,0,0,0,0,0)
    player3 = player(0,0,0,0,0,0,0,0,0)
    player4 = player(0,0,0,0,0,0,0,0,0)
    player_list = [player1,player2,player3,player4]
    while five > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addFive()
    while hundred > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addHundred()
    while fifty > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addFifty()
    while ten > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addTen()
    while ppf > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addP()
    while gpf > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addG()
    while epf > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addE()
    while spf > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addS()
    while cpf > 0:
        lowest = min(player1.total(), player2.total(), player3.total(), player4.total())
        lowest_player = findLowest(player_list,lowest)
        lowest_player.addC()
    diff1 = player1.total() - per_player
    gems1 = (player1.ten * 10) + (player1.fifty * 50) + (player1.hundred * 100) + (player1.five * 500)
    msg1 = ('Player1 recieves: ' + str(player1.pp) + 'P, ' + str(player1.gp) + 'G, ' + str(player1.ep) + 'E, ' + str(player1.sp) + 'S, ' + str(player1.cp) + 'C, and ' + str(gems1) + ' worth of gems, ' + 'with a difference of ' + str(diff1))
    diff2 = player2.total() - per_player
    gems2 = (player2.ten * 10) + (player2.fifty * 50) + (player2.hundred * 100) + (player2.five * 500)
    msg2 = ('Player2 recieves: ' + str(player2.pp) + 'P, ' + str(player2.gp) + 'G, ' + str(player2.ep) + 'E, ' + str(player2.sp) + 'S, ' + str(player2.cp) + 'C, and ' + str(gems2) + ' worth of gems, ' + 'with a difference of ' + str(diff2))
    diff3 = player3.total() - per_player
    gems3 = (player3.ten * 10) + (player3.fifty * 50) + (player3.hundred * 100) + (player3.five * 500)
    msg3 = ('Player3 recieves: ' + str(player3.pp) + 'P, ' + str(player3.gp) + 'G, ' + str(player3.ep) + 'E, ' + str(player3.sp) + 'S, ' + str(player3.cp) + 'C, and ' + str(gems3) + ' worth of gems, ' + 'with a difference of ' + str(diff3))
    diff4 = player4.total() - per_player
    gems4 = (player4.ten * 10) + (player4.fifty * 50) + (player4.hundred * 100) + (player4.five * 500)
    msg4 = ('Player4 recieves: ' + str(player4.pp) + 'P, ' + str(player4.gp) + 'G, ' + str(player4.ep) + 'E, ' + str(player4.sp) + 'S, ' + str(player4.cp) + 'C, and ' + str(gems4) + ' worth of gems, ' + 'with a difference of ' + str(diff4))
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)

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

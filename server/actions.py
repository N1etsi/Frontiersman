from enum import Enum
from elements import Resources as Resources
from elements import ExtraResources as ExtraResources
import random

class ActionType(Enum):
    TRADE = 0
    BUY = 1
    ROLL = 3
    SPECIAL = 4
    END = 5

class BuyType(Enum):
    SETTLEMENT = 0
    CITY = 1
    ROAD = 2
    SPECIALCARD = 3

class SpecialType(Enum):
    ROADS2 = 0
    ROBBER = 1
    VICTORYPOINT = 2 #Hidden victory point
    MONOPOLY = 3 #Get all the card from one resource (except from bank)
    FREECHOICE2 = 4 #Choose 2 cards of choice to receive from the bank


class Action():
    def __init__(self, type):
        self.type = type

#ERRORS HERE
#TODO TRADES
class Trade(Action):
    def offer(self, board, player, give, want):
        instantTrade = False
        impossible = False
        if  enoughResources(player, give):
            if len(give) < 2 and len(want) < 2:
                resPort = board.getNeiPorts()
                for res1 in give:
                    for res2 in want:
                        if board.bank.resStock.resource[res2] > want[res2]:
                            for prt in resPort:
                                if res1 == prt.resource and give[res1] == 2 and want[res2] == 1:
                                    instantTrade = True
                            for prt in resPort:
                                if prt.resource == ExtraResources.ANY and give[res1] == 3 and want[res2] == 1:
                                    instantTrade = True
                            if give[res1] == 4 and want[res2] == 1:
                                instantTrade = True
        else:
            impossible = True

        if impossible:
            return None

        elif instantTrade:
            player.hand.removeCard(res1, give[res1])
            player.hand.addCard(res2, want[res2])

            board.bank.resStock.addCard(res1, give[res1])
            board.bank.resStock.removeCard(res2, want[res2])

        else:
            pass
            #TODO ask players if they want to trade

        def acceptOffer(plrA, giveA, plrB, giveB):
            if  enoughResources(plrA, giveA) and enoughResources(plrB, giveB):
                for res1 in giveA:
                    plrA.hand.removeCard(res1, giveA[res1])
                    plrB.hand.addCard(res1, giveA[res1])

                for res2 in giveB:
                    plrA.hand.addCard(res2, want[res2])

                plrB.hand.addCard(res1, give[res1])
                plrB.hand.removeCard(res2, want[res2])





class Buy(Action):
    buyCost = {
        BuyType.SETTLEMENT: {
            Resources.WOOL : 1,
            Resources.GRAIN : 1,
            Resources.LUMBER : 1,
            Resources.BRICK : 1
        },
        BuyType.CITY : {
            Resources.GRAIN : 2,
            Resources.ORE : 3
        },
        BuyType.ROAD : {
            Resources.LUMBER : 1,
            Resources.BRICK : 1
        },
        BuyType.SPECIALCARD : {
            Resources.WOOL : 1,
            Resources.GRAIN : 1,
            Resources.ORE : 1,
        }
    }

    def build(self, board, player, typeB, coord):
        if enoughResources(player, buyCost[typeB]):
            removeResources(board, player, buyCost[typeB])
            if typeB == self.BuyType.SETTLEMENT:
                board.placeSettlement(player, coord)
            elif typeB == self.BuyType.CITY:
                board.upgradeSettlement(player, coord)
            elif typeB == self.BuyType.ROAD:
                board.placeRoad(player, coord)
            elif typeB == self.SPECIALCARD:
                board.getSpecialCard(player)
            else:
                print("WRONG BUY TYPE")

            return True
        else:
            return False

    def enoughResources(self, player, buyCost):
        enough = True

        for res in Resources:
            if res in buyCost:
                if buyCost[res] > player.hand.cardCountType(res):
                    enough = False
                    break

        return enough

    def removeResources(board, player, buyCost):
        if not enoughResources(player, buyCost):
            return False

        for res in Resources:
            if res in buyCost:
                player.hand.removeCard(res, buyCost[res])
                board.bank.resStock.addCard(res, buyCost[res])


        return True

class Roll(Action):
    def Dice(maxV, nDice=1):
        tot = 0

        for i in range(nDice):
            tot += random.randint(1, maxV)

        return tot

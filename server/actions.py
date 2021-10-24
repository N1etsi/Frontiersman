from enum import Enum
from elements import Resources
from elements import ExtraResources
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


def diceRoll(board):
    tot = 0

    for i in range(board.diceNum):
        tot += random.randint(1, board.diceSize)

    for ti in board.tiles:
        if ti.num == tot:
            board.distributeResources(ti)

    return tot

#BUY
def buy(board, player, typeB, coord):
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

def enoughResources(player, buyCost):
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

#OFFER EXAMPLE
offer = {
    Resources.WOOL : 1,
    Resources.GRAIN : 1,
    Resources.ORE : 1,
}
request = {
    Resources.WOOL : 1,
    Resources.GRAIN : 1,
    Resources.ORE : 1,
}


#TRADE
def trade(board, player, offer, request):
    n_offer = len(offer)
    n_req = len(request)

    bank = False

    if player.hand.hasFunds(offer):

        if n_offer == 1 and n_req == 1:
            amountOffer = list(offer.values())[0])
            typeOffer = list(offer.keys())[0])
            amountReq = list(offer.values())[0])

            st, qnt = board.availablePort(player, typeOffer)

            if amountOffer==qnt and amountReq==1:
                bank = True
                tradeCardsBank(player, offer, request)

        #Not an automatic trade, propose to trade
        if not bank:
            ## TODO: Domestic trades (needs server working to facilitate development)
            pass


def tradeCardsBank(player, offer, request):
    for type in offer:
        player.hand.removeCard(type, offer[type])

    for type in request:
        player.hand.addCard(type, request[type])

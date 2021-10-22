from enum import Enum
from elements import Resources as Resources
from elements import ExtraResources as ExtraResources

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


class Action():
    def __init__(self, type):
        self.type = type

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

    def __init__(self, board, player, typeA, typeB, coord = None):
        super.__init__(typeA)
        self.build(board, player, typeB, coord)

    def build(self, board, player, typeB, coord):
        if enoughResources(player, buyCost[ypeB]):
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

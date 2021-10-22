from enum import Enum
from elements import Resources as Resources
from elements import ExtraResources as ExtraResources

class ActionType(Enum):
    TRADE = 0
    BUILD = 1
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
    buildCost = {
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


    def __init__(self, typeA):
        super.__init__(typeA, typeB)

    #def build(self, type):

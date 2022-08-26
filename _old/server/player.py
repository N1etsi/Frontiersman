import elements
import board
from enum import Enum

class PlayersC(Enum):
    NONE = 0
    BLUE = 1
    ORANGE = 2
    RED = 3
    GREEN = 4
    PURPLE = 5
    BROWN = 6
    DARK_GREEN = 7
    DARK_BLUE = 8
    DARK_RED = 9
    BLACK = 10
    WHITE = 11
    BANK = 100

class Player():
    def __init__(self, user):
        self.user = user

        self.hand = elements.Hand(self)

        self.score = 0

        self.LongestRoad = 0
        self.ArmySize = 0

        self.roadsBuilt = 0
        self.settlementsBuilt = 0
        self.cityBuilt = 0


class Bank():
    def __init__(self):
        self.resStock = elements.Hand(PlayersC.BANK)

        self.maxResources = 19
        self.maxSpecCards = 25
        self.maxRoads = 15
        self.maxSettlements = 5
        self.maxCities = 4

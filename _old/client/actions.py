from enum import Enum

class ActionType(Enum):
    TRADE = 0
    BUILD = 1
    BUY = 2
    ROLL = 3
    SPECIAL = 4
    END = 5

class Action():
    def __self__(self, type):
        self.type = type

#class Trade(Action):






for tip in ActionType:
    print(tip)

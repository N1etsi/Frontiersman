import elements
import board

class Player():
    def __init__(self, user):
        self.User = user

        self.hand = elements.Hand(self)

        self.score = 0

        self.LongestRoad = 0
        self.ArmySize = 0

        self.roadsBuilt = 0
        self.settlementsBuilt = 0
        self.cityBuilt = 0


class Bank():
    def __init__(self):
        self.stock = elements.Hand()

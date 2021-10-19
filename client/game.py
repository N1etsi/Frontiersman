from enum import Enum
import random

class Resources(Enum):
    DESERT = 0
    WOOL = 1
    GRAIN = 2
    BRICK = 3
    LUMBER = 4
    ORE = 5


class Tile():
    def __init__(self):
        self.coord = None
        self.type = None
        self.num = random.randint(1, 12)

    def __init__(self, coord, type):
        self.coord = coord
        self.type = type
        self.num = random.randint(1, 12)



#class Road():

#class Settlement():

#class Robber():


#GAME LOGIC FUN
def getRandomResource(des=0):
    while True:
        type = random.choice(list(Resources))
        if not(type == Resources.DESERT and des == 1):
            break

    return type

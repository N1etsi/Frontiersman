from enum import Enum
import random

class Resources(Enum):
    DESERT = 0
    WOOL = 1
    GRAIN = 2
    BRICK = 3
    LUMBER = 4
    ORE = 5

class ExtraResources(Enum):
    GOLD = 0
    ANY = 1

class Players(Enum):
    WHITE = 0
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



class Tile():
    def __init__(self):
        self.coord = None
        self.type = None
        self.num = random.randint(1, 12)

    def __init__(self, coord, type):
        self.coord = coord
        self.type = type
        self.num = random.randint(1, 12)


#side of the road relative to tile is expressed with the dir var (direction)
#0, 1 and 2 are possible values, top left, top and top right
#the bottom of ones are the top of the others, so only 3 are necessary
class Road():
    def __init__(self, player, tile, dir):
        self.tile = tile
        self.dir = dir

        self.player = player

#settlement coords are the ones of the tile on their top
#easy to calculate the other 2 this way, (add one to z and either -1 to x or y while the other is 0)
#class Settlement():

#originally on the desert
#class Robber():

#how many
#how to define the trade ratio
# use of extra resources enum??
#class Port():


#GAME LOGIC FUN
def getRandomResource(des=0):
    while True:
        type = random.choice(list(Resources))
        if not(type == Resources.DESERT and des == 1):
            break

    return type

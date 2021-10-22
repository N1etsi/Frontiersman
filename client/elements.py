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


class Tile():
    def __init__(self):
        self.coord = None
        self.type = None
        self.num = random.randint(1, 12)
        self.tilerect=None
        self.tilesurface=None
        self.numsurface=None
        

    def __init__(self, coord, type):
        self.coord = coord
        self.type = type
        self.num = random.randint(1, 12)

    def axis2to3(self, coord):
        z = -coord[0]-coord[1]
        coord.append(z)
        return coord

    def axis3(self):
        newcoord.append(coord[0])
        newcoord.append(coord[1])
        z = -coord[0]-coord[1]
        newcoord.append(z)
        return newcoord


class Vertex():
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

        sum = self.i+self.j+self.k
        if sum > 0 or sum < -1:
            print("invalid point")
            return None

    def __eq__(self, newV):
        if self.i==newV.i and self.j==newV.j and self.k==newV.k:
            return True
        else:
            return False

    def __ne__(self, newV):
        return not self.__eq__(newV)


    #True for positive, False for negative
    #True when neighbours align with the positive axis reference
    def polarity(self):
        if (self.i+self.j+self.k) == -1:
            return True
        else:
            return False

    def toString(self):
        return '('+str(self.i)+','+str(self.j)+','+str(self.k)+')'

#side of the road relative to tile is expressed with the dir var (direction)
#0, 1 and 2 are possible values, top left, top and top right
#the bottom of ones are the top of the others, so only 3 are necessary
class Road():
    def __init__(self, player, vertPair):
        self.player = player
        self.vertPair = vertPair

        #enforce polarity
        if self.vertPair[0].polarity():
            temp = self.vertPair[0]
            self.vertPair[0] = self.vertPair[1]
            self.vertPair[1] = temp

    def __eq__(self, newR):
        if self.vertPair[0] == newR.vertPair[0] and self.vertPair[1] == newR.vertPair[1]:
            return True
        else:
            return False

    def __ne__(self, newR):
        return not self.__eq__(newR)

    def toString(self):
        str = "Road: "
        str +=self.vertPair[0].toString()+" to "+self.vertPair[1].toString()

        return str


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

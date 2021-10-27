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

class Items(Enum):
    HOUSE = 0
    CASTLE = 1


class Item():
    def __init__(self, type, rect, surface, mask):
        self.type=type
        self.rect=rect
        self.surface=surface
        self.mask=mask



class Tile():
    def __init__(self, coord, type):
        self.coord = coord
        self.type = type
        self.num = random.randint(1, 12)
        self.tilerect=None #DELETE
        self.tilesurface=None #DELETE
        self.numsurface=None #DELETE


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

class Hand():
    def __init__(self, player):
        self.player = player
        self.resources = {}
        self.resourceCount = 0
        self.special = {}
        self.specialCount = 0

        for rs in Resources:
            self.resources[rs] = 0

    def addCard(self, type, qnt=1):
        self.resources[type] += qnt
        self.resourceCount += qnt

    def removeCard(self, type, qnt=1):
        delt = self.resources[type] - qnt

        if delt >= 0:
            self.resources[type] -= qnt
            self.resourceCount -= qnt
            return qnt

        else:
            return 0



#settlement coords are the ones of the tile on their top
#easy to calculate the other 2 this way, (add one to z and either -1 to x or y while the other is 0)
class Settlement():
    def __init__(self, player, vertex):
        self.player = player
        self.loc = vertex
        self.city = False

    def evolveToCity(self):
        self.city = True


class Robber():
    def __init__(self, tile):
        self.loc = tile

    def move(self, tile):
        self.loc = tile

    def rob(self, player, victim):
        robbed = False
        if victim.hand.resourceCount > 0:
            while True:
                res = getRandomResource(1)
                if (victim.hand.removeCard(res, 1)) > 0:
                    player.hand.addCard(res)
                    robbed = True
                    break

        return robbed



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

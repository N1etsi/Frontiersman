import random
from enum import Enum
import elements
import Player

class Board:
    def __init__(self, size=3, nplayers=1):
        self.sideSize = size
        self.nplayers = nplayers
        self.tiles = []
        self.roads = []
        self.settlements = []
        self.players = []
        self.getRandomBoard(size)

        self.bank = user.Player()

        self.gameOver = False



    def getRandomBoard(self, S):
        des = 0

        for x in range(-S+1, S):
            for y in range(-S+1, S):
                z = -x-y
                if z < S and z > -S:
                    #var change so it starts the list from the top
                    coord = [y, -x-y]
                    type = elements.Tile.getRandomResource(des)
                    if type == elements.Resources.DESERT:
                            des = 1
                    self.tiles.append(elements.Tile(coord, type))

        if des == 0:
            while True:
                x = random.randint(-S+1,S-1)
                y = random.randint(-S+1,S-1)
                z = -x-y
                if z <= S-1:
                    break


            desertTile = self.getTile([x,y])
            desertTile.type = elements.Resources.DESERT

        return self.tiles

    def getTile(self, coord):
        return next((tile for tile in self.tiles if tile.coord == coord), None)

    #Gives back roads connected to the user's selected road on the specified polarity
    def searchNextRoadPolar(self, road, polarity):
        if polarity:
            indP = 1
        elif not polarity:
            indP = 0

        vert = road.vertPair[indP]


        nei = []

        for road_iter in board.roads:
            if road_iter.player == road.player:
                if vert == road_iter.vertPair[indP] and road_iter != road:
                    nei.append(road_iter)

        return nei

    #GAME LOGIC
    def placeRoad(self, player, vertPair):
        newRoad = elements.Road(player, vertPair)
        board.roads.append(newRoad)
        #player.addedRoad(newRoad)

        return newRoad

    def placeSettlement(self, player, vertex):
        x = 5

    def upgradeSettlement(self, player, vertex):
        x = 5

    #STILL NEEDS TO KEEP VISITED STACK TO AVOID LOOPS
    #NEEDS TO CHECK IF SETTLEMENTS ARE BUILT ON THAT VERTEX (only from other players)
    def getLongestRoad(self, player, newR):
        length = 1
        negLength = 0
        posLength = 0
        pol = 0

        stack = []

        negLength, stack = recWorker(newR, 0, 0, stack)
        posLength, stack = recWorker(newR, 1, 0, stack)

        print(negLength,posLength)
        return length + negLength + posLength

    #Recursive worker to find longest path
    def recWorker(self, road, polarity, length, stack):
        neis = board.searchNextRoadPolar(road, polarity)

        maxL = 0
        maxStack = []
        stack.append(road)

        if len(neis) <= 0:
            newStack = copy.deepcopy(stack)
            return length, newStack
        else:
            for newR in neis:
                if newR not in stack:
                    newStack = copy.deepcopy(stack)
                    L, M = self.recWorker(newR, 1-polarity, length+1, newStack)
                    if L > maxL:
                        maxL = L
                        maxStack = M


        return maxL, maxStack

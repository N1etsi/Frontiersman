import random
from enum import Enum
import elements

class Board:
    def __init__(self, size=3, nplayers=1):
        self.sideSize = size
        self.nplayers = nplayers
        self.tiles = []
        self.roads = []
        self.settlements = []
        self.getRandomBoard(size)


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

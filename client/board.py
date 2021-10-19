import game as game
import random


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

                    type = game.getRandomResource(des)
                    if type == game.Resources.DESERT:
                            des = 1

                    self.tiles.append(game.Tile(coord, type))

        if des == 0:
            while True:
                x = random.randint(-S+1,S-1)
                y = random.randint(-S+1,S-1)
                z = -x-y
                if z <= S-1:
                    break


            desertTile = self.getTile([x,y])
            desertTile.type = game.Resources.DESERT

        return self.tiles

    def placeRoad(self, player, tile, dir):
        newRoad = game.Road(player, tile, dir)
        self.roads.append(newRoad)


    def getTile(self, coord):
        return next((tile for tile in self.tiles if tile.coord == coord), None)

    def countLongestRoad(self, player):
        





#GP Methods
def axis3to2(coord):
    z = -coord[0]-coord[1]
    coord.append(z)
    return coord



if __name__=="__main__":

    board = Board(2)
    board.placeRoad(game.Players.WHITE, board.getTile([0, -1]), 1)

    for road in board.roads:
        print(road.tile.coord, road.dir)

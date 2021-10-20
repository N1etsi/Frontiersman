import elements
import random
import player


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

                    type = elements.getRandomResource(des)
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

    #roads are placed with the negative point first
    def placeRoad(self, player, vertPair):
        newRoad = elements.Road(player, vertPair)
        self.roads.append(newRoad)
        #player.addedRoad(newRoad)

        return newRoad


    def getTile(self, coord):
        return next((tile for tile in self.tiles if tile.coord == coord), None)

    def countLongestRoad(self, player):
        for road in self.roads:
            if road.player == player:
                len = 0
                searched = []
                search.append(road)


    def searchRoadNei(self, player, road):
        vert0 = road.vertPair[0]
        vert1 = road.vertPair[1]

        if vert0.polarity():
            indSearch = 1
        else:
            indSearch = 0

        nei = []

        for road in board.roads:
            if road.player == player:
                if road.vertPair[indSearch]==vert0 or road.vertPair[1-indSearch]==vert1:
                    nei.append(road)

        return nei



#def tiles



if __name__=="__main__":

    board = Board(2)

    road1=board.placeRoad(elements.Players.WHITE, [elements.Vertex(0,0,0), elements.Vertex(0,0,-1)])
    road2=board.placeRoad(elements.Players.WHITE, [elements.Vertex(0,0,-1), elements.Vertex(1,0,-1)])


    for road in board.roads:
        print(road.vertPair[0].toString(), road.vertPair[1].toString())


    print(board.searchRoadNei(elements.Players.WHITE, road2)[1].vertPair[0].toString())

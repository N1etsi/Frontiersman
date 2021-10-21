import elements
import random
import player
import copy


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

    #STILL NEEDS TO KEEP VISITED STACK TO AVOID LOOPS
    #NEEDS TO CHECK IF SETTLEMENTS ARE BUILT ON THAT VERTEX (only from other players)
    def getLongestRoad(self, player, newR):
        length = 1
        negLength = 0
        posLength = 0
        pol = 0

        stack = []



        negLength, stack = self.recWorker(newR, 0, 0, stack)

        print("eree")
        posLength, stack = self.recWorker(newR, 1, 0, stack)

        print(negLength,posLength)
        return length + negLength + posLength


    #Recursive worker to find longest path
    def recWorker(self, road, polarity, length, stack):
        neis = self.searchNextRoadPolar(road, polarity)
        for r in neis:
            print(r.toString())
        print(" ")
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




if __name__=="__main__":
    board = Board(2)
    plr = elements.Players.WHITE
    road1=board.placeRoad(plr, [elements.Vertex(0,0,0), elements.Vertex(0,0,-1)])
    road2=board.placeRoad(plr, [elements.Vertex(0,0,-1), elements.Vertex(1,0,-1)])
    road3=board.placeRoad(plr, [elements.Vertex(1,0,-2), elements.Vertex(1,0,-1)])
    road4=board.placeRoad(plr, [elements.Vertex(1,0,-2), elements.Vertex(1,1,-2)])
    road5=board.placeRoad(plr, [elements.Vertex(0,1,-2), elements.Vertex(1,1,-2)])
    road6=board.placeRoad(plr, [elements.Vertex(0,1,-2), elements.Vertex(0,1,-1)])
    #road7=board.placeRoad(plr, [elements.Vertex(-1,1,-1), elements.Vertex(0,1,-1)])
    road7=board.placeRoad(plr, [elements.Vertex(0,0,-1), elements.Vertex(0,1,-1)])

    print(board.getLongestRoad(plr, road5))

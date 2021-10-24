import random
from enum import Enum
import copy
import elements
import player
from elements import Vertex


class Board:
    def __init__(self, players, size=3):
        #Game Settings
        self.sideSize = size
        self.nplayers = len(players)
        print("num players ", self.nplayers)
        self.diceSize = 6
        self.diceNum = 2

        #Game StateVars
        self.turn = 0
        self.round = 0
        self.gameOver = False

        self.tiles = []
        self.roads = []
        self.settlements = []
        self.ports = []
        self.players = players
        self.robber = None

        self.getRandomBoard(size)

        self.bank = player.Bank()



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
                    self.tiles.append(elements.Tile(coord, type, self.diceSize*self.diceNum))

        if des == 0:
            while True:
                x = random.randint(-S+1,S-1)
                y = random.randint(-S+1,S-1)
                z = -x-y
                if z <= S-1:
                    break


            desertTile = self.getTile([x,y])
            desertTile.type = elements.Resources.DESERT
            self.robber = Robber(desertTile)

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

    def getNeiVertices(self, v):
        pol = -1
        if v.polarity():
            pol = 1

        iNei = elements.Vertex(v.i+pol, v.j, v.k)
        jNei = elements.Vertex(v.i, v.j+pol, v.k)
        kNei = elements.Vertex(v.i, v.j, v.k+pol)

        neis = []

        if iNei is not None:
            neis.append(iNei)
        if jNej is not None:
            neis.append(jNej)
        if kNek is not None:
            neis.append(kNek)

        return neis

    def getSettlement(self, player, vert):
        ind = 0
        if vert.polarity():
            ind = 1

        for st in self.settlements:
            if st.player == player and st.vertPair[ind]==vert:
                return st

        return None

    def distributeResources(self, tile):
        mult = 1
        surrSet = self.getSurroundingSettlements(tile)

        for set in surrSet:
            if set.city:
                mult = 2
            set.player.hand.addCard(tile.type, 1*mult)

    def getSurroundingSettlements(self, tile):
        surrSet = []
        c = tile.coord
        possVert = []
        z = -c[0]-c[1]
        possVert.append(Vertex(   c[0],    c[1],   z))
        possVert.append(Vertex(-1+c[0],    c[1],   z))
        possVert.append(Vertex(   c[0], -1+c[1],   z))
        possVert.append(Vertex(-1+c[0],    c[1], 1+z))
        possVert.append(Vertex(   c[0], -1+c[1], 1+z))
        possVert.append(Vertex(-1+c[0], -1+c[1], 1+z))

        for st in self.settlements:
            for vert in possVert:
                if st.loc == vert:
                    surrSet.append(st)

        return surrSet



    def getNeiPorts(self, player):
        neiPorts = []
        for st in self.settlements:
            if st.player == player:
                for prts in self.ports:
                    for prt in prts.locs:
                        if st.loc == prt.locs:
                            neiPorts.append(prts)

        return neiPorts


    #GAME LOGIC
    def placeRoad(self, player, vertPair):
        reach = False
        ind = 0
        if vertPair[0].polarity():
            ind = 1
        newRoad = elements.Road(player, vertPair)

        for rd in self.roads:
            if rd == newRoad:
                del newRoad
                reach = False
                break
            if rd.player == player:
                if rd.vertPair[0] == vertPair[ind] or rd.vertPair[1] == vertPair[1-ind]:
                    reach = True


        if reach == False:
            return None

        board.roads.append(newRoad)
        player.roadsBuilt += 1

        newSize = getLongestRoad(player, newRoad)

        if player.LongestRoad < newSize:
            player.LongestRoad = newSize

        return newRoad

    def placeSettlement(self, player, vert):
        reach = False
        occupied = False

        #Calc ocupation
        all = getNeiVertices(vert)
        all.append(vert)
        for set in self.settlements:
            for ver in all:
                if set.loc == ver:
                    occupied = True
                    return not occupied
        #Calc reach of road
        ind = 0
        if vert.polarity():
            ind = 1

        for rd in self.roads:
            if rd.player == player and rd.vertPair[ind] == vert:
                reach = True
        if reach == False:
            return reach

        newSet = elements.Settlement(player, vert)
        board.settlements.append(newSet)
        player.settlementsBuilt += 1

        return newSet


    def upgradeSettlement(self, player, vertex):
        st = self.getSettlement(player, vertex)

        st.evolveToCity()


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

    def nexRound(self):
        if self.turn >= self.nplayers:
            self.turn = 0
            self.round +=1


        ind = self.turn

        if self.round == 1:
            ind = self.nplayers - self.turn - 1

        self.turn += 1
        return self.players[ind]

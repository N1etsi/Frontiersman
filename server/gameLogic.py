import copy
#GP Game Logic Methods

def placeRoad(board, player, vertPair):
    newRoad = elements.Road(player, vertPair)
    board.roads.append(newRoad)
    #player.addedRoad(newRoad)

    return newRoad

def placeSettlement(self):
    x = 5

#STILL NEEDS TO KEEP VISITED STACK TO AVOID LOOPS
#NEEDS TO CHECK IF SETTLEMENTS ARE BUILT ON THAT VERTEX (only from other players)
def getLongestRoad(board, player, newR):
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
def recWorker(board, road, polarity, length, stack):
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

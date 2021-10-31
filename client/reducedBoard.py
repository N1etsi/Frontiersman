import elements
import random
import player

class reducedBoard:
    def __init__(self, size, rPlayers, tiles, roads, settlements, hand):
        self.sideSize = size
        self.reducedPlayers = rPlayers #[]
        self.tiles = tiles#[]
        self.roads = roads#[]
        self.settlements = settlements#[]

        self.hand = hand

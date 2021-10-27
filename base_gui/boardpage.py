import pygame
import pygame_gui


class boardpage():
    wTile = 80
    hTile = 80*1.155

    gTiles = []
    gRoads = []
    gSettlements = []
    gCards = []



    def __init__(self,manager, mainH, mainW):
        self.manager = manager
        self.H = mainH
        self.W = mainW

        self.centerX = 3*self.W/8 - self.wTile/2
        self.centerY = 3*self.H/8 - self.hTile/3

        self.margin = 6
        #Tile unitary offset of tile coordinate system
        self.yOff = 3*(self.hTile+self.margin)/4
        self.xOff = (self.wTile+self.margin)/2

        self.zoomlimit=self.wTile



    def handleEvent(self, event):
        print("Nothing")

    def setupBoard(self):
        pass
        #LOAD IMAGE ASSETS

    def enable(self):
        pass
        #START DRAWING

import pygame
import pygame_gui

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from elements import *





class boardpage():
    wTile = 80
    hTile = 80*1.155

    gTiles = []
    gRoads = []
    gSettlements = []
    gCards = []



    def __init__(self,manager, mainH, mainW, board, screen):
        self.manager = manager
        self.H = mainH
        self.W = mainW
        self.gameBoard = board
        self.screen = screen

        self.centerX = 3*self.W/8 - self.wTile/2
        self.centerY = 3*self.H/8 - self.hTile/3

        self.margin = 6
        #Tile unitary offset of tile coordinate system
        self.yOff = 3*(self.hTile+self.margin)/4
        self.xOff = (self.wTile+self.margin)/2

        self.zoomlimit=self.wTile

        self.tile_size=(self.wTile,self.hTile)
        self.number_size=(self.wTile/3,self.hTile/3)
        self.road_size=(self.margin,self.wTile/2)
        self.dice_size=(50,50)

        self.d1=1
        self.d2=1


    def handleEvent(self, event):
        pass

    def setupBoard(self):
        self.initTiles()
        self.initNumbers()
        self.initItems()
        self.initDices()
        self.updateDicts()

        pass
        #LOAD IMAGE ASSETS

    def draw(self):
        self.drawBoard()
        print("draw")
        pass
        #START DRAWING

    def initTiles(self):
        self.sea = pygame.image.load("./client/gui/assets/tiles/sea.png")
        self.sea = pygame.transform.scale(self.sea, self.tile_size)
        self.tilemask = pygame.mask.from_surface(self.sea)

        self.desert = pygame.image.load("./client/gui/assets/tiles/desert.png")
        self.desert = pygame.transform.scale(self.desert, self.tile_size)

        self.brick = pygame.image.load("./client/gui/assets/tiles/brick.png")
        self.brick = pygame.transform.scale(self.brick, self.tile_size)

        self.grain = pygame.image.load("./client/gui/assets/tiles/grain.png")
        self.grain = pygame.transform.scale(self.grain, self.tile_size)

        self.lumber = pygame.image.load("./client/gui/assets/tiles/lumber.png")
        self.lumber = pygame.transform.scale(self.lumber, self.tile_size)

        self.ore = pygame.image.load("./client/gui/assets/tiles/ore.png")
        self.ore = pygame.transform.scale(self.ore, self.tile_size)

        self.wool = pygame.image.load("./client/gui/assets/tiles/wool.png")
        self.wool = pygame.transform.scale(self.wool, self.tile_size)



    def initNumbers(self):
        self.one = pygame.image.load("./client/gui/assets/numbers/one.png")
        self.one = pygame.transform.scale(self.one, self.number_size)

        self.two = pygame.image.load("./client/gui/assets/numbers/two.png")
        self.two = pygame.transform.scale(self.two, self.number_size)

        self.three = pygame.image.load("./client/gui/assets/numbers/three.png")
        self.three = pygame.transform.scale(self.three, self.number_size)

        self.four = pygame.image.load("./client/gui/assets/numbers/four.png")
        self.four = pygame.transform.scale(self.four, self.number_size)

        self.five = pygame.image.load("./client/gui/assets/numbers/five.png")
        self.five = pygame.transform.scale(self.five, self.number_size)

        self.six = pygame.image.load("./client/gui/assets/numbers/six.png")
        self.six = pygame.transform.scale(self.six, self.number_size)

        self.seven = pygame.image.load("./client/gui/assets/numbers/seven.png")
        self.seven = pygame.transform.scale(self.seven, self.number_size)

        self.eigth = pygame.image.load("./client/gui/assets/numbers/eigth.png")
        self.eigth = pygame.transform.scale(self.eigth, self.number_size)

        self.nine = pygame.image.load("./client/gui/assets/numbers/nine.png")
        self.nine = pygame.transform.scale(self.nine, self.number_size)

        self.ten = pygame.image.load("./client/gui/assets/numbers/ten.png")
        self.ten = pygame.transform.scale(self.ten, self.number_size)

        self.eleven = pygame.image.load("./client/gui/assets/numbers/eleven.png")
        self.eleven = pygame.transform.scale(self.eleven, self.number_size)

        self.twelve = pygame.image.load("./client/gui/assets/numbers/twelve.png")
        self.twelve = pygame.transform.scale(self.twelve, self.number_size)

        self.num_list=[None,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eigth,self.nine,self.ten,self.eleven,self.twelve]

        self.updateDicts()

        for tile in self.gameBoard.tiles:
            x = float(self.centerX + (tile.coord[0]-tile.coord[1])*self.xOff)
            y = float(self.centerY + (tile.coord[0]+tile.coord[1])*self.yOff)
            tile.tilerect = (float(x), float(y), float(self.wTile), float(self.hTile))
            tile.tilesurface = self.surfaceDict[tile.type]
            tile.numsurface = self.num_list[tile.num]

    def initItems(self):
        #TODO
        pass

    def initDices(self):
        self.done = pygame.image.load("./client/gui/assets/dices/one.png")
        self.done = pygame.transform.scale(self.done, self.dice_size)

        self.dtwo = pygame.image.load("./client/gui/assets/dices/two.png")
        self.dtwo = pygame.transform.scale(self.dtwo, self.dice_size)

        self.dthree = pygame.image.load("./client/gui/assets/dices/three.png")
        self.dthree = pygame.transform.scale(self.dthree, self.dice_size)

        self.dfour = pygame.image.load("./client/gui/assets/dices/four.png")
        self.dfour = pygame.transform.scale(self.dfour, self.dice_size)

        self.dfive = pygame.image.load("./client/gui/assets/dices/five.png")
        self.dfive = pygame.transform.scale(self.dfive, self.dice_size)

        self.dsix = pygame.image.load("./client/gui/assets/dices/six.png")
        self.dsix = pygame.transform.scale(self.dsix, self.dice_size)

        self.dice_list=[None,self.done,self.dtwo,self.dthree,self.dfour,self.dfive,self.dsix]

        self.dicemask = pygame.mask.from_surface(self.done)

    def updateDicts(self):
        self.resources = {
                Resources.WOOL : 20,
                Resources.GRAIN : 2,
                Resources.BRICK : 8,
                Resources.LUMBER : 4,
                Resources.ORE : 5
        }

        self.surfaceDict = {
              Resources.DESERT: self.desert,
              Resources.WOOL: self.wool,
              Resources.GRAIN: self.grain,
              Resources.BRICK: self.brick,
              Resources.LUMBER: self.lumber,
              Resources.ORE: self.ore
            }

        self.buyCost = {
            BuyType.HOUSE: {
                Resources.WOOL : 1,
                Resources.GRAIN : 1,
                Resources.LUMBER : 1,
                Resources.BRICK : 1
            },
            BuyType.CASTLE : {
                Resources.GRAIN : 2,
                Resources.ORE : 3
            },
            BuyType.ROAD : {
                Resources.LUMBER : 1,
                Resources.BRICK : 1
            },
            BuyType.SPECIALCARD : {
                Resources.WOOL : 1,
                Resources.GRAIN : 1,
                Resources.ORE : 1,
            }
        }

    def drawBoard(self):
        for tile in self.gameBoard.tiles:
            self.screen.blit(self.surfaceDict[tile.type], (tile.tilerect[0],tile.tilerect[1]))
            x_num = tile.tilerect[0] + tile.tilerect[2]/3
            y_num = tile.tilerect[1] + tile.tilerect[3]/10
            if tile.type != Resources.DESERT:
                self.screen.blit(self.num_list[tile.num],(x_num,y_num))


class BuyType(Enum):
    HOUSE = 0
    CASTLE = 1
    ROAD = 2
    SPECIALCARD = 3

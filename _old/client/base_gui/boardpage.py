import pygame
import pygame_gui

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from elements import *





class boardpage():

    gTiles = []
    gRoads = []
    gSettlements = []
    gCards = []



    def __init__(self,manager, mainH, mainW, board, screen, bg):
        self.manager = manager
        self.H = mainH
        self.W = mainW
        self.gameBoard = board
        self.screen = screen
        self.bg = bg

        self.wTile = self.W/20
        self.hTile = self.wTile*1.155

        self.centerX = 3*self.W/8 - 3*self.wTile/4
        self.centerY = 3*self.H/8 - 1*self.hTile/4

        self.margin = self.hTile/25
        #Tile unitary offset of tile coordinate system
        self.yOff = 3*(self.hTile+2*self.margin)/4
        self.xOff = (self.wTile+self.margin)/2

        self.zoomlimit=self.wTile


        self.dice_size=(self.wTile/2,self.wTile/2)

        self.settlement_size = (self.wTile/2+3*self.margin/4,self.H/6+self.margin)

        self.panel_size = (3*self.W/10, self.H/5)
        self.slim_panel_size = (3*self.W/10, self.H/8)
        self.long_panel_size = (6*self.W/10, self.H/5)

        self.card_size = ( (self.panel_size[0]-8*self.margin)/6,self.panel_size[1]-4*self.margin)

        self.d1=1
        self.d2=1

        self.elem = []
        self.panels = []


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
        #print("draw")
        pass
        #START DRAWING

    def initTiles(self):
        self.tile_size = (self.wTile, self.hTile) #(w,h)

        self.sea = pygame.image.load("./client/gui/assets/tiles/sea.png")
        self.sea = pygame.transform.smoothscale(self.sea, self.tile_size)
        self.tilemask = pygame.mask.from_surface(self.sea)

        self.desert = pygame.image.load("./client/gui/assets/tiles/desert.png")
        self.desert = pygame.transform.smoothscale(self.desert, self.tile_size)

        self.brick = pygame.image.load("./client/gui/assets/tiles/brick.png")
        self.brick = pygame.transform.smoothscale(self.brick, self.tile_size)

        self.grain = pygame.image.load("./client/gui/assets/tiles/grain.png")
        self.grain = pygame.transform.smoothscale(self.grain, self.tile_size)

        self.lumber = pygame.image.load("./client/gui/assets/tiles/lumber.png")
        self.lumber = pygame.transform.smoothscale(self.lumber, self.tile_size)

        self.ore = pygame.image.load("./client/gui/assets/tiles/ore.png")
        self.ore = pygame.transform.smoothscale(self.ore, self.tile_size)

        self.wool = pygame.image.load("./client/gui/assets/tiles/wool.png")
        self.wool = pygame.transform.smoothscale(self.wool, self.tile_size)

    def initNumbers(self):
        self.number_size = (self.wTile/3,self.hTile/3)

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
        #Settlements
        loadedSettlement = pygame.image.load('./client/base_gui/assets/general/settlement.png')



        self.initBuy()
        self.initBank()
        self.initHand()

        #mockups
        pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((7*self.W/10 - self.margin, 2*self.H/5 + 16*self.margin),
                                                                        self.slim_panel_size),
                                                        starting_layer_height = 1,
                                                        manager = self.manager)

        pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((7*self.W/10 - self.margin, 2*self.H/5 + self.slim_panel_size[1] + 18*self.margin),
                                                                        self.slim_panel_size),
                                                        starting_layer_height = 1,
                                                        manager = self.manager)

        self.hidePanel()
        pass

    def initBuy(self):
        movingW = self.margin
        singleW = self.settlement_size[0]
        self.buyPanel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((7*self.W/10 - self.margin, 12*self.margin),
                                                                        self.panel_size),
                                                        starting_layer_height = 1,
                                                        manager = self.manager)
        settlement_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((movingW, self.margin), self.settlement_size),
                                                    text="",
                                                    object_id ="#settlement",
                                                    container = self.buyPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        city_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((movingW, self.margin), self.settlement_size),
                                                    text="",
                                                    object_id ="#city",
                                                    container = self.buyPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        road_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((movingW, self.margin), self.settlement_size),
                                                    text="",
                                                    object_id ="#road",
                                                    container = self.buyPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        spec_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((movingW, self.margin), self.settlement_size),
                                                    text="",
                                                    object_id ="#spec",
                                                    container = self.buyPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        skip_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((movingW, self.margin), (3*self.settlement_size[0]/4+5, self.settlement_size[1])),
                                                    text="",
                                                    object_id ="#skip",
                                                    container = self.buyPanel,
                                                    manager=self.manager)

        self.panels.append(self.buyPanel)

    def initBank(self):
        movingW = self.margin
        singleW = self.card_size[0]

        self.bankPanel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((6*self.W/10 - self.margin, 1*self.H/5 + 14*self.margin),
                                                                        self.panel_size),
                                                        starting_layer_height = 1,
                                                        manager = self.manager)
        self.panels.append(self.bankPanel)

        imgBank = pygame.image.load("./client/base_gui/assets/general/bank.png")
        self.bankIco = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((movingW, self.margin), self.card_size),
                                                    image_surface = imgBank,
                                                    container = self.bankPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        imgLumber = pygame.image.load("./client/base_gui/assets/cards/lumber.png")
        self.lumberIco = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((movingW, self.margin), self.card_size),
                                                    image_surface = imgLumber,
                                                    container = self.bankPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        imgBrick = pygame.image.load("./client/base_gui/assets/cards/brick.png")
        self.lumberIco = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((movingW, self.margin), self.card_size),
                                                    image_surface = imgBrick,
                                                    container = self.bankPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        imgWool = pygame.image.load("./client/base_gui/assets/cards/wool.png")
        self.lumberIco = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((movingW, self.margin), self.card_size),
                                                    image_surface = imgWool,
                                                    container = self.bankPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        imgGrain = pygame.image.load("./client/base_gui/assets/cards/grain.png")
        self.lumberIco = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((movingW, self.margin), self.card_size),
                                                    image_surface = imgGrain,
                                                    container = self.bankPanel,
                                                    manager=self.manager)

        movingW += singleW + self.margin
        imgOre = pygame.image.load("./client/base_gui/assets/cards/ore.png")
        self.lumberIco = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((movingW, self.margin), self.card_size),
                                                    image_surface = imgOre,
                                                    container = self.bankPanel,
                                                    manager=self.manager)



    def initHand(self):

        self.handPanel = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((4*self.W/10 - self.margin, 4*self.H/5 - 2*self.margin),
                                                                        self.long_panel_size),
                                                        starting_layer_height = 1,
                                                        manager = self.manager)
        self.panels.append(self.handPanel)


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

    def enable(self):
        for pa in self.panels:
            pa.show()


    def hide(self):
        for el in self.elem:
            el.hide()

        self.screen.blit(self.bg, (0, 0))

    def hidePanel(self):
        for panel in self.panels:
            panel.hide()

        self.screen.blit(self.bg, (0, 0))

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

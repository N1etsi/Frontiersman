import pygame
import time
from enum import Enum
import random
import math
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(1, parent_dir)
import board
import elements
import random

class BuyType(Enum):
    HOUSE = 0
    CASTLE = 1
    ROAD = 2
    SPECIALCARD = 3

class guiGame():
    def __init__(self):
        self.run=True
        self.W = 1080
        self.H = 720

        self.wTile = 80
        self.hTile = 80*1.155 #1.16 * self.wTile

        self.centerX = 3*self.W/8 - self.wTile/2
        self.centerY = 3*self.H/8 - self.hTile/3

        self.margin = 6
        self.yOff = 3*self.hTile/4+3*self.margin
        self.xOff = (self.wTile+self.margin)/2

        self.board_size=(self.W, self.H)
        self.zoomlimit=self.wTile
        self.screen= pygame.display.set_mode(self.board_size, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE | pygame.NOFRAME)
        pygame.display.set_caption('Frontiersman')
        self.screen.fill([37,100,184])
        self.tile_size=(self.wTile,self.hTile)
        self.number_size=(self.wTile/3,self.hTile/3)
        self.road_size=(self.margin,self.wTile/2)
        self.dice_size=(50,50)
        self.d1=1
        self.d2=1


        self.initAssets()

        self.gameBoard = board.Board(3)

        plr = elements.Players.GREEN
        road1=self.gameBoard.placeRoad(plr, [elements.Vertex(0,0,0), elements.Vertex(0,0,-1)])
        road2=self.gameBoard.placeRoad(plr, [elements.Vertex(0,0,-1), elements.Vertex(1,0,-1)])
        road3=self.gameBoard.placeRoad(plr, [elements.Vertex(1,0,-2), elements.Vertex(1,0,-1)])
        road4=self.gameBoard.placeRoad(plr, [elements.Vertex(1,0,-2), elements.Vertex(1,1,-2)])
        road5=self.gameBoard.placeRoad(plr, [elements.Vertex(0,1,-2), elements.Vertex(1,1,-2)])
        road6=self.gameBoard.placeRoad(plr, [elements.Vertex(0,1,-2), elements.Vertex(0,1,-1)])

        self.initWindow()

        self.main()

    def initWindow(self):
        for tile in self.gameBoard.tiles:
            x = float(self.centerX + (tile.coord[0]-tile.coord[1])*self.xOff)
            y = float(self.centerY + (tile.coord[0]+tile.coord[1])*self.yOff)
            tile.tilerect = (float(x), float(y), float(self.wTile), float(self.hTile))
            tile.tilesurface = self.typedict[tile.type]
            tile.numsurface = self.num_list[tile.num]

    def windowevents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode(event.dict['size'], pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
                for tile in self.gameBoard.tiles:
                    tile.tilesurface = pygame.transform.smoothscale(self.typedict[tile.type], (tile.tilerect[2],tile.tilerect[3]))
                    self.tilemask=pygame.mask.from_surface(tile.tilesurface)
                    tile.numsurface = pygame.transform.smoothscale(self.num_list[tile.num], (tile.tilerect[2]/3,tile.tilerect[3]/3))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (event.button == 5 and self.zoomlimit > 0.1*self.wTile or event.button == 4 and self.zoomlimit < 2*self.wTile):
                    zoom = 1.5 if event.button == 4 else 0.75
                    self.mx, self.my = event.pos
                    for tile in self.gameBoard.tiles:
                        left   = float(self.mx + (tile.tilerect[0] - self.mx) * zoom)
                        right  = float(self.mx + (tile.tilerect[0] + tile.tilerect[2] - self.mx) * zoom)
                        top    = float(self.my + (tile.tilerect[1] - self.my) * zoom)
                        bottom = float(self.my + (tile.tilerect[1] + tile.tilerect[3] - self.my) * zoom)
                        self.zoomlimit = right-left
                        tile.tilerect = (float(left), float(top), float(right - left), float(bottom - top))
                        tile.tilesurface = pygame.transform.smoothscale(self.typedict[tile.type], (tile.tilerect[2],tile.tilerect[3]))
                        self.tilemask=pygame.mask.from_surface(tile.tilesurface)
                        tile.numsurface = pygame.transform.smoothscale(self.num_list[tile.num], (tile.tilerect[2]/3,tile.tilerect[3]/3))

                if (event.button == 3):
                    self.mx,self.my = event.pos
                    self.pan()

                if (event.button == 1):
                    for tile in self.gameBoard.tiles:
                        try:
                            if self.tilemask.get_at((event.pos[0]-tile.tilerect[0], event.pos[1]-tile.tilerect[1])):
                                print(tile.type)
                        except IndexError:
                            pass

                    for item in self.items:
                        try:
                            if item.mask.get_at((event.pos[0]-item.rect[0], event.pos[1]-item.rect[1])):
                                print(item.type)
                        except IndexError:
                            pass
                    for i in range(2):
                        try:
                            if self.dicemask.get_at((event.pos[0]-900+60*i, event.pos[1]-600)):
                                self.d1=random.randint(1,6)
                                self.d2=random.randint(1,6)
                        except IndexError:
                            pass

    def displaygame(self):

        self.displayboard()
        self.displayhand()
        self.displayRoads()
        self.displayprice()
        self.displaydices()

        pygame.display.flip()

    def displaydices(self):
        # d1=random.randint(1, 6)
        # print(d1)
        self.screen.blit(self.dice_list[self.d1], (900,600))
        self.screen.blit(self.dice_list[self.d2], (960,600))

    def displayboard(self):
        self.screen.fill([37,100,184])
        for tile in self.gameBoard.tiles:
            self.screen.blit(tile.tilesurface, (tile.tilerect[0],tile.tilerect[1]))
            x_num = tile.tilerect[0] + tile.tilerect[2]/3
            y_num = tile.tilerect[1] + tile.tilerect[3]/10
            if tile.type != elements.Resources.DESERT:
                self.screen.blit(tile.numsurface,(x_num,y_num))

        for item in self.items:
            self.screen.blit(item.surface, (item.rect[0],item.rect[1]))

    def displayhand(self):
        count=0
        for res in elements.Resources:
            if res in self.resources:
                #print(self.resources[res])
                for i in range(self.resources[res]):
                    if i>8:
                        break
                    self.screen.blit(self.typedict[res],(50+count+10*i,600))
                count=count+i*10+50

    def displayprice(self):

        for item in self.items:
            try:
                if item.mask.get_at((pygame.mouse.get_pos()[0]-item.rect[0], pygame.mouse.get_pos()[1]-item.rect[1])):
                    for buy in self.buyCost:
                        if buy == item.type:
                            #print(self.buyCost[buy])
                            count=0
                            for res in elements.Resources:
                                if res in self.buyCost[buy]:
                                    #print(self.buyCost[buy][res])
                                    for i in range(self.buyCost[buy][res]):
                                        if i>8:
                                            break
                                        self.screen.blit(self.typedict[res],(item.rect[0]+count+10*i,item.rect[1]-100))
                                    count=count+i*10+50
            except IndexError:
                pass

    def displayRoads(self):

        for rd in self.gameBoard.roads:
            #pass
            vert0 = rd.vertPair[0]
            vert1 = rd.vertPair[1]


            x0 = self.centerX + (vert0.i-vert0.j + 1)*(self.wTile + self.margin)/2 - self.margin/2
            y0 = self.centerY + (2*vert0.k -vert0.i-vert0.j)*(self.hTile + self.margin)/4 - self.margin/2

            x1 = self.centerX + (vert1.i-vert1.j + 1)*(self.wTile + self.margin)/2 - self.margin/2
            y1 = self.centerY + (2*vert1.k -vert1.i-vert1.j)*(self.hTile + self.margin)/4 - self.margin/2


            pygame.draw.line(self.screen, (20, 200, 140), (x0, y0), (x1, y1), round(self.margin*1.30))

    def pan(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if (event.button == 3):
                        return
            nx, ny = pygame.mouse.get_pos()
            for tile in self.gameBoard.tiles:
                left   = float(tile.tilerect[0] + (nx - self.mx))
                right  = float(tile.tilerect[0] + tile.tilerect[2] + (nx - self.mx))
                top    = float(tile.tilerect[1] + (ny - self.my))
                bottom = float(tile.tilerect[1] + tile.tilerect[3] + (ny - self.my))
                tile.tilerect = (float(left), float(top), float(right - left), float(bottom - top))
                #print(tile.tilerect)
            self.displaygame()
            self.mx=nx
            self.my=ny

    def updatedicts(self):
        self.resources = {
                elements.Resources.WOOL : 20,
                elements.Resources.GRAIN : 2,
                elements.Resources.BRICK : 8,
                elements.Resources.LUMBER : 4,
                elements.Resources.ORE : 5
        }

        self.buyCost = {
            BuyType.HOUSE: {
                elements.Resources.WOOL : 1,
                elements.Resources.GRAIN : 1,
                elements.Resources.LUMBER : 1,
                elements.Resources.BRICK : 1
            },
            BuyType.CASTLE : {
                elements.Resources.GRAIN : 2,
                elements.Resources.ORE : 3
            },
            BuyType.ROAD : {
                elements.Resources.LUMBER : 1,
                elements.Resources.BRICK : 1
            },
            BuyType.SPECIALCARD : {
                elements.Resources.WOOL : 1,
                elements.Resources.GRAIN : 1,
                elements.Resources.ORE : 1,
            }
        }

    def main(self):

        self.run=True
        while self.run:
            self.windowevents()
            self.updatedicts()
            self.displaygame()





            # x_road1= x - self.margin
            # y_road1= y + self.hTile/4
            #
            # x_road23= x + self.wTile/2
            # y_road23= y
            #
            # self.screen.blit(self.gray,(x_road1,y_road1))
            # self.screen.blit(self.gray60,(x_road23,y_road23))
            # self.screen.blit(self.gray300,(x_road23,y_road23))

            ##roads
            #pygame.draw.line(self.screen, (0, 255, 0), (x - self.margin/2, y + self.hTile/4), (x - self.margin/2, y + 3*self.hTile/4), self.margin)
            # pygame.draw.line(self.screen, (0, 255, 0), (x - self.margin/2, y + self.hTile/4), (x - self.margin/2, y + 3*self.hTile/4), self.margin)
            # pygame.draw.line(self.screen, (0, 255, 0), (x - self.margin/2, y + self.hTile/4), (x - self.margin/2, y + 3*self.hTile/4), self.margin)
        pygame.quit()

    def initAssets(self):
        self.initTiles()
        self.initNumbers()
        self.initRoads()
        self.initItems() #
        self.initDices()

    def initItems(self):
        self.items = []

        housecoords=(550,600,140,100)
        housesurface = pygame.image.load("./client/gui/assets/builds/house.png")
        housesurface = pygame.transform.smoothscale(housesurface, (housecoords[2],housecoords[3]))
        #self.itemsurface=housesurface
        housemask = pygame.mask.from_surface(housesurface)
        self.items.append(elements.Item(BuyType.HOUSE, housecoords, housesurface, housemask))

        castlecoords=(700,600,140,100)
        castlesurface = pygame.image.load("./client/gui/assets/builds/castle.png")
        castlesurface = pygame.transform.smoothscale(castlesurface, (castlecoords[2],castlecoords[3]))
        #self.itemsurface=housesurface
        castlemask = pygame.mask.from_surface(castlesurface)
        self.items.append(elements.Item(BuyType.CASTLE, castlecoords, castlesurface, castlemask)) ## TODO:

    def initTiles(self):
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

        self.typedict = {
              elements.Resources.DESERT: self.desert,
              elements.Resources.WOOL: self.wool,
              elements.Resources.GRAIN: self.grain,
              elements.Resources.BRICK: self.brick,
              elements.Resources.LUMBER: self.lumber,
              elements.Resources.ORE: self.ore
            }

    def initNumbers(self):
        self.one = pygame.image.load("./client/gui/assets/numbers/one.png")
        self.one = pygame.transform.smoothscale(self.one, self.number_size)

        self.two = pygame.image.load("./client/gui/assets/numbers/two.png")
        self.two = pygame.transform.smoothscale(self.two, self.number_size)

        self.three = pygame.image.load("./client/gui/assets/numbers/three.png")
        self.three = pygame.transform.smoothscale(self.three, self.number_size)

        self.four = pygame.image.load("./client/gui/assets/numbers/four.png")
        self.four = pygame.transform.smoothscale(self.four, self.number_size)

        self.five = pygame.image.load("./client/gui/assets/numbers/five.png")
        self.five = pygame.transform.smoothscale(self.five, self.number_size)

        self.six = pygame.image.load("./client/gui/assets/numbers/six.png")
        self.six = pygame.transform.smoothscale(self.six, self.number_size)

        self.seven = pygame.image.load("./client/gui/assets/numbers/seven.png")
        self.seven = pygame.transform.smoothscale(self.seven, self.number_size)

        self.eigth = pygame.image.load("./client/gui/assets/numbers/eigth.png")
        self.eigth = pygame.transform.smoothscale(self.eigth, self.number_size)

        self.nine = pygame.image.load("./client/gui/assets/numbers/nine.png")
        self.nine = pygame.transform.smoothscale(self.nine, self.number_size)

        self.ten = pygame.image.load("./client/gui/assets/numbers/ten.png")
        self.ten = pygame.transform.smoothscale(self.ten, self.number_size)

        self.eleven = pygame.image.load("./client/gui/assets/numbers/eleven.png")
        self.eleven = pygame.transform.smoothscale(self.eleven, self.number_size)

        self.twelve = pygame.image.load("./client/gui/assets/numbers/twelve.png")
        self.twelve = pygame.transform.smoothscale(self.twelve, self.number_size)

        self.num_list=[None,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eigth,self.nine,self.ten,self.eleven,self.twelve]

    def initDices(self):
        self.done = pygame.image.load("./client/gui/assets/dices/one.png")
        self.done = pygame.transform.smoothscale(self.done, self.dice_size)

        self.dtwo = pygame.image.load("./client/gui/assets/dices/two.png")
        self.dtwo = pygame.transform.smoothscale(self.dtwo, self.dice_size)

        self.dthree = pygame.image.load("./client/gui/assets/dices/three.png")
        self.dthree = pygame.transform.smoothscale(self.dthree, self.dice_size)

        self.dfour = pygame.image.load("./client/gui/assets/dices/four.png")
        self.dfour = pygame.transform.smoothscale(self.dfour, self.dice_size)

        self.dfive = pygame.image.load("./client/gui/assets/dices/five.png")
        self.dfive = pygame.transform.smoothscale(self.dfive, self.dice_size)

        self.dsix = pygame.image.load("./client/gui/assets/dices/six.png")
        self.dsix = pygame.transform.smoothscale(self.dsix, self.dice_size)

        self.dice_list=[None,self.done,self.dtwo,self.dthree,self.dfour,self.dfive,self.dsix]

        self.dicemask = pygame.mask.from_surface(self.done)

    def initRoads(self):
        self.black = pygame.image.load("./client/gui/assets/roads/black.png")
        self.black = pygame.transform.scale(self.black, self.road_size)
        self.black60 = pygame.transform.rotate(self.black, 60)
        self.black300 = pygame.transform.rotate(self.black, 300)


        self.blue = pygame.image.load("./client/gui/assets/roads/blue.png")
        self.blue = pygame.transform.scale(self.blue, self.road_size)
        self.blue60 = pygame.transform.rotate(self.blue, 60)
        self.blue300 = pygame.transform.rotate(self.blue, 300)


        self.brown = pygame.image.load("./client/gui/assets/roads/brown.png")
        self.brown = pygame.transform.scale(self.brown, self.road_size)
        self.brown60 = pygame.transform.rotate(self.brown, 60)
        self.brown300 = pygame.transform.rotate(self.brown, 300)

        self.dark_blue = pygame.image.load("./client/gui/assets/roads/dark_blue.png")
        self.dark_blue = pygame.transform.scale(self.dark_blue, self.road_size)
        self.dark_blue60 = pygame.transform.rotate(self.dark_blue, 60)
        self.dark_blue300 = pygame.transform.rotate(self.dark_blue, 300)

        self.dark_green = pygame.image.load("./client/gui/assets/roads/dark_green.png")
        self.dark_green = pygame.transform.scale(self.dark_green, self.road_size)
        self.dark_green60 = pygame.transform.rotate(self.dark_green, 60)
        self.dark_green300 = pygame.transform.rotate(self.dark_green, 300)

        self.gray = pygame.image.load("./client/gui/assets/roads/default.png")
        self.gray = pygame.transform.scale(self.gray, self.road_size)
        self.gray60 = pygame.transform.rotate(self.gray, 60)
        self.gray300 = pygame.transform.rotate(self.gray, 300)

        self.green = pygame.image.load("./client/gui/assets/roads/green.png")
        self.green = pygame.transform.scale(self.green, self.road_size)
        self.green60 = pygame.transform.rotate(self.green, 60)
        self.green300 = pygame.transform.rotate(self.green, 300)

        self.orange = pygame.image.load("./client/gui/assets/roads/orange.png")
        self.orange = pygame.transform.scale(self.orange, self.road_size)
        self.orange60 = pygame.transform.rotate(self.orange, 60)
        self.orange300 = pygame.transform.rotate(self.orange, 300)

        self.purple = pygame.image.load("./client/gui/assets/roads/purple.png")
        self.purple = pygame.transform.scale(self.purple, self.road_size)
        self.purple60 = pygame.transform.rotate(self.purple, 60)
        self.purple300 = pygame.transform.rotate(self.purple, 300)

        self.red = pygame.image.load("./client/gui/assets/roads/red.png")
        self.red = pygame.transform.scale(self.red, self.road_size)
        self.red60 = pygame.transform.rotate(self.red, 60)
        self.red300 = pygame.transform.rotate(self.red, 300)

        self.white = pygame.image.load("./client/gui/assets/roads/white.png")
        self.white = pygame.transform.scale(self.white, self.road_size)
        self.white60 = pygame.transform.rotate(self.white, 60)
        self.white300 = pygame.transform.rotate(self.white, 300)

        self.yellow = pygame.image.load("./client/gui/assets/roads/yellow.png")
        self.yellow = pygame.transform.scale(self.yellow, self.road_size)
        self.yellow60 = pygame.transform.rotate(self.yellow, 60)
        self.yellow300 = pygame.transform.rotate(self.yellow, 300)

g = guiGame()

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

class guiGame():
    def __init__(self):
        self.run=True
        self.W = 1080
        self.H = 720

        self.wTile = 80
        self.hTile = 80*1.16 #1.16 * self.wTile

        self.centerX = 3*self.W/8 - self.wTile/2
        self.centerY = 3*self.H/8 - self.hTile/3

        self.margin = 6
        self.yOff = 3*(self.hTile+self.margin)/4
        self.xOff = (self.wTile+self.margin)/2

        self.board_size=(self.W, self.H)
        self.zoomlimit=self.wTile
        self.screen= pygame.display.set_mode(self.board_size, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
        pygame.display.set_caption('Frontiersman')
        self.screen.fill([37,100,184])
        self.tile_size=(self.wTile,self.hTile)
        self.number_size=(self.wTile/3,self.hTile/3)
        self.road_size=(self.margin,self.wTile/2)

        self.initAssets()

        self.gameBoard = board.Board(5)

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
                        tile.numsurface = pygame.transform.smoothscale(self.num_list[tile.num], (tile.tilerect[2]/3,tile.tilerect[3]/3))

                if (event.button == 1):
                    self.mx,self.my = event.pos
                    self.pan()

    def displaygame(self):
        self.screen.fill([37,100,184])
        for tile in self.gameBoard.tiles:
            self.screen.blit(tile.tilesurface, (tile.tilerect[0],tile.tilerect[1]))
            x_num = tile.tilerect[0] + tile.tilerect[2]/3
            y_num = tile.tilerect[1] + tile.tilerect[3]/10
            self.screen.blit(tile.numsurface,(x_num,y_num))
        pygame.display.flip()

    def pan(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if (event.button == 1):
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


    def main(self):

        self.run=True
        while self.run:
            self.windowevents()
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

    def initTiles(self):
        self.sea = pygame.image.load("./client/gui/assets/tiles/sea.png")
        self.sea = pygame.transform.scale(self.sea, self.tile_size)

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

        self.num_list=[self.one,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eigth,self.nine,self.ten,self.eleven,self.twelve]

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

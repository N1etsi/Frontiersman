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
        self.W = 1080
        self.H = 720

        self.wTile = 50
        self.hTile = 58

        self.centerX = 3*self.W/8 - self.wTile/2
        self.centerY = 3*self.H/8 - self.hTile/3

        self.margin = 6
        self.yOff = 3*(self.hTile+self.margin)/4
        self.xOff = (self.wTile+self.margin)/2

        self.board_size=(self.W, self.H)
        self.screen= pygame.display.set_mode(self.board_size)
        pygame.display.set_caption('Frontiersman')
        self.screen.fill([37,100,184])
        self.tile_size=(self.wTile,self.hTile)
        self.number_size=(self.wTile/3,self.hTile/3)

        self.initAssets()

        gameBoard = board.Board(5)

        for tile in gameBoard.tiles:
            x = self.centerX + (tile.coord[0]-tile.coord[1])*self.xOff
            y = self.centerY + (tile.coord[0]+tile.coord[1])*self.yOff

            self.screen.blit(self.typedict[tile.type], (x,y))

            x_num = x + 20
            y_num = y + 20
            self.screen.blit(self.num_list[tile.num],(x_num,y_num))

        pygame.display.flip()
        time.sleep(10)

    def initAssets(self):
        self.initTiles()
        self.initNumbers()

    def initTiles(self):
        self.sea = pygame.image.load("./client/gui/assets/tiles/sea.jpg")
        self.sea = pygame.transform.scale(self.sea, self.tile_size)

        self.desert = pygame.image.load("./client/gui/assets/tiles/desert.gif")
        self.desert = pygame.transform.scale(self.desert, self.tile_size)

        self.brick = pygame.image.load("./client/gui/assets/tiles/brick.gif")
        self.brick = pygame.transform.scale(self.brick, self.tile_size)

        self.grain = pygame.image.load("./client/gui/assets/tiles/grain.gif")
        self.grain = pygame.transform.scale(self.grain, self.tile_size)

        self.lumber = pygame.image.load("./client/gui/assets/tiles/lumber.gif")
        self.lumber = pygame.transform.scale(self.lumber, self.tile_size)

        self.ore = pygame.image.load("./client/gui/assets/tiles/ore.gif")
        self.ore = pygame.transform.scale(self.ore, self.tile_size)

        self.wool = pygame.image.load("./client/gui/assets/tiles/wool.gif")
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

g = guiGame()

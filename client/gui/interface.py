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
import game


def init_display():
    W = 720
    H = 480

    wTile = 50
    hTile = 58

    centerX = 3*W/8
    centerY = 3*H/8

    margin = 10
    yOff = 3*(hTile+margin)/4
    xOff = (wTile+margin)/2

    size=75
    
    board_size=(W, H)
    screen= pygame.display.set_mode(board_size)
    pygame.display.set_caption('Catan')
    tile_size=(wTile,hTile)

    #Init Tiles

    sea = pygame.image.load("./client/gui/assets/tiles/sea.jpg")
    sea = pygame.transform.scale(sea, tile_size)

    desert = pygame.image.load("./client/gui/assets/tiles/desert.gif")
    desert = pygame.transform.scale(desert, tile_size)

    brick = pygame.image.load("./client/gui/assets/tiles/brick.gif")
    brick = pygame.transform.scale(brick, tile_size)

    grain = pygame.image.load("./client/gui/assets/tiles/grain.gif")
    grain = pygame.transform.scale(grain, tile_size)

    lumber = pygame.image.load("./client/gui/assets/tiles/lumber.gif")
    lumber = pygame.transform.scale(lumber, tile_size)

    ore = pygame.image.load("./client/gui/assets/tiles/ore.gif")
    ore = pygame.transform.scale(ore, tile_size)

    wool = pygame.image.load("./client/gui/assets/tiles/wool.gif")
    wool = pygame.transform.scale(wool, tile_size)

    typedict = {
          game.Resources.DESERT: desert,
          game.Resources.WOOL: wool,
          game.Resources.GRAIN: grain,
          game.Resources.BRICK: brick,
          game.Resources.LUMBER: lumber,
          game.Resources.ORE: ore
        }

    print('Init finished!!!')

    gameBoard = board.Board(5)

    for tile in gameBoard.tiles:
        x = centerX + (tile.coord[0]-tile.coord[1])*xOff
        y = centerY + (tile.coord[0]+tile.coord[1])*yOff

        screen.blit(typedict[tile.type], (x,y))


    pygame.display.flip()
    time.sleep(10)

init_display()

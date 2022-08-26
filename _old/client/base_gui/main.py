import random
import pygame
import pygame_gui
import mainpage
import boardpage
import globpage
from pages import *
import client

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)




W = 1900
H = 1000

bW = 200
bH= 50

board = client.getBoard()

currPage = Pages.MAIN


pygame.display.init()
pygame.init()
pygame.display.set_caption('Frontiersman')
window_surface = pygame.display.set_mode((W, H),  pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE | pygame.NOFRAME)
manager = pygame_gui.UIManager((W, H), "./client/base_gui/assets/themes/button_theme.json")
background = pygame.Surface((W, H))
background.fill(pygame.Color([37,100,184])) #2564b8

globP = globpage.globpage(manager, H,W,25,25)
mainP = mainpage.mainpage(manager, H,W,bH,bW, window_surface, background)
boardP = boardpage.boardpage(manager, H,W, board, window_surface, background)

globP.setupGlob()
mainP.setupMain()
boardP.setupBoard()

clock = pygame.time.Clock()
is_running = True
reloadPage = False



while is_running:
    time_delta = clock.tick(60)/1000.0
    if reloadPage:
        if currPage == Pages.MAIN:
            mainP.enable()
        elif currPage == Pages.BOARD:
            boardP.enable()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        globP.handleEvent(event)

        if currPage == Pages.MAIN:
            reloadPage, currPage = mainP.handleEvent(event)

        elif currPage == Pages.BOARD:
            boardP.handleEvent(event)



        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    if currPage == Pages.BOARD:
        boardP.draw()
    manager.draw_ui(window_surface)

    pygame.display.update()


pygame.display.quit()
pygame.quit()
sys.exit()

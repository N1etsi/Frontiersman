import pygame
import pygame_gui
import sys
from pages import *

class mainpage():
    def __init__(self,manager, mainH, mainW, bH, bW, screen, bg):
        self.manager = manager
        self.mainH = mainH
        self.mainW = mainW

        self.bH = bH
        self.bW = bW

        self.screen = screen
        self.bg = bg

        self.loggedIn = False

        self.elements = []

    def buttonFirstPage(self):
        self.start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect( ((self.mainW-self.bW)/2, (self.mainH-self.bH)/2 + 2.5 *self.bH) , (self.bW,self.bH)),
                                                    text="LOG IN",
                                                    manager=self.manager)

        self.join_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect( ((self.mainW-self.bW)/2, (self.mainH-self.bH)/2 + 4*self.bH) , (self.bW,self.bH)),
                                                    text="JOIN GAME",
                                                    manager=self.manager)

        self.create_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect( ((self.mainW-self.bW)/2, (self.mainH-self.bH)/2 + 5.5*self.bH) , (self.bW,self.bH)),
                                                    text="CREATE GAME",
                                                    manager=self.manager)

        self.elements.append(self.start_button)
        self.elements.append(self.join_button)
        self.elements.append(self.create_button)

    def logo(self):
        loadedLogo = pygame.image.load('./client/base_gui/assets/general/logo.png')
        imgLogo = pygame_gui.elements.UIImage(pygame.Rect(((self.mainW/2-1.5*self.bW),(self.mainH/4-3*self.bH)), (3*self.bW, 2*self.bW) ),
                                    loadedLogo, self.manager)

        self.elements.append(imgLogo)



    def setupMain(self):
        self.logo()
        self.buttonFirstPage()

        if not self.loggedIn:
            self.join_button.disable()
            self.create_button.disable()

    def handleEvent(self, event):

        if (event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_element == self.join_button):
                self.hideMain()
                return True, Pages.BOARD

        elif (event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_element == self.start_button):
                self.loggedInU()

                return False, Pages.MAIN


        else:
            return False, Pages.MAIN

    def hideMain(self):
        for el in self.elements:
            el.hide()

        self.screen.blit(self.bg, (0, 0))

    def enable(self):
        for el in self.elements:
            el.show()

    def loggedInU(self):
        self.loggedIn = True
        self.join_button.enable()
        self.create_button.enable()

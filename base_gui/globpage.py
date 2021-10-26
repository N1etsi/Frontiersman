import pygame
import pygame_gui
import sys
from pages import *

class globpage():
    def __init__(self,manager, mainH, mainW, cH, cW):
        self.manager = manager
        self.mainH = mainH
        self.mainW = mainW

        self.cH = cH
        self.cW = cW

        self.elements = []

    def statButtons(self):
        self.close_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect( (self.mainW-20-self.cW, 20) , (self.cH,self.cW)),
                                                    text = "",
                                                    manager=self.manager,
                                                    object_id = "#sqbutton"
                                                    )
        self.move_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect( (self.mainW-60-self.cW, 20) , (self.cH,self.cW)),
                                                    text = "",
                                                    manager=self.manager,
                                                    object_id = "#sqbutton"
                                                    )

        self.elements.append(self.close_button)
        self.elements.append(self.move_button)

    def handleEvent(self, event):
        if (event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_element == self.close_button):
                pygame.display.quit()
                pygame.quit()
                sys.exit()


    def setupGlob(self):
        self.statButtons()

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from elements import *

class guiBoard():
    def __init__(self, board):
        self.board = board
        self.loadGUIelements()

    def loadGUIelements(self):
        for tile in board.tiles:




class guiTile(Tile):
    def __init__(self, coord, type, tilerect, tilesurface, numsurface, tsize, nsize):
        super().__init__(coord, type)
        self.tileRect=tilerect
        self.tileSurface=tilesurface
        self.numSurface=numsurface




class guiRoad(Road):
    pass

class guiSettlement(Settlement):
    pass

class guiCard():
    pass
    type

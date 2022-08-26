from tkinter import *
from math import cos, sin, sqrt, radians, pi
import numpy as np


#------------------------------------------------------------------------------
class FillHexagon:
    def __init__(self, parent, c, length, color, tags):
        self.parent = parent # canvas
        self.x = c[0]           # top left x
        self.y = c[1]           # top left y
        self.length = length # length of a side
        self.color = color   # fill color

        self.selected = False
        self.tags = tags
        
        self.draw()

    def draw(self):
        start_x = self.x
        start_y = self.y
        r = self.length
        coords = [(start_x+r*cos(pi*x/3+pi/6),start_y+r*sin(pi*x/3+pi/6)) for x in range(6)]
        
        self.parent.create_polygon(coords[0][0],
                                   coords[0][1], 
                                   coords[1][0], 
                                   coords[1][1],
                                   coords[2][0],
                                   coords[2][1],
                                   coords[3][0],
                                   coords[3][1],
                                   coords[4][0],
                                   coords[4][1], 
                                   coords[5][0],
                                   coords[5][1], 
                                   fill=self.color,
                                   outline="gray",
                                   tags=self.tags)
                                   
class FillVert:
    def __init__(self, parent, c, length, margin, color, tags):
        self.parent = parent # canvas
        self.x = c[0]           # top left x
        self.y = c[1]           # top left y
        self.length = length # length of a side
        self.color = color   # fill color
        self.rad = self.length / 6
        self.margin = margin

        self.selected = False
        self.tags = tags
        
        self.draw()

    def draw(self):
        x = self.x
        y = self.y + self.length + self.margin
        r = self.rad

        
        
        self.parent.create_oval(x-r,y-r,x+r,y+r, tags=self.tags)

#---------------------------------------------------------
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Hexagon Grid")
        self.can = Canvas(self, width=800, height=600, bg="#a1e2a1")
        self.can.pack()
        self.can.bind("<Button-1>", self.click)

        self.w = 800# self.winfo_screenwidth()
        self.h = 600# self.winfo_screenheight()
        self.r = self.w / 20
        self.mar = self.r/5


        self.hexagons = []
        self.vertices = []
        self.initGrid(3)


        
    def initGrid(self, sz):
        
        transf_x = sqrt(3) * self.r
        transf_y = -self.r
        transf = np.array((transf_x, transf_y))

        c_x = self.w / 2
        c_y = self.h / 2


        for q in range(-sz+1, sz):
            for r in range(-sz+1, sz):
                s = -q -r
                if s < sz and s> -sz:
                    x = (q+r/2)* sqrt(3) * (self.r+self.mar) 
                    y = (-r) *    1.5    * (self.r+self.mar)
                    coord = np.array([x,y]) + np.array([c_x, c_y])


                    h = FillHexagon(self.can,
                                coord,
                                self.r,
                                "#a1e2a1",
                                "{}.{}.H".format(q, r))

                    self.hexagons.append(h)

                    v = FillVert(self.can, coord, self.r, self.mar, "#a1e2a1", "{}.{}.V".format(q, r))

                    self.vertices.append(v)

          

    def click(self, evt):
        x , y = evt.x, evt.y
        print(x, y)
        for i in self.hexagons:
            i.selected = False
            i.isNeighbour = False
            self.can.itemconfigure(i.tags, fill=i.color)
        print(self.can.find_closest(x,y)[0])
        clicked = self.can.find_closest(x, y)[0] # find closest
        print(" Tag:" , self.can.gettags(clicked)[0])

        for i in self.hexagons: # re-configure selected only
            if i.selected:
                self.can.itemconfigure(i.tags, fill="#53ca53")
            if i.isNeighbour:
                self.can.itemconfigure(i.tags, fill="#76d576")

#----------------------------------------------------------
if __name__ =='__main__':
    app = App()
    app.mainloop()
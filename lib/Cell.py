from math import sqrt

class Cell:
    def __init__(self, x, y):
        self.type = 0 #0 is empty, 1 is full
        self.x = x
        self.y = y
        self.h = 0
        self.g = 1
        self.f = 0
        self.parent = None

    def get_type(self):
        return self.type
    
    def set_type(self, cell_type):
        self.type = cell_type

    def calc_h(self, END):
        dx = abs(self.x - END.x)
        dy = abs(self.y - END.y)
        self.h = (dx+dy)+(sqrt(2)-2)*min(dx, dy) 

    def calc_f(self):
        self.f = self.h + self.g

    def calc_g(self, parent_g):
        self.g += parent_g.g

    def get_g(self):
        return self.g
    
    def get_f(self):
        return self.f
    
    def set_parent(self, parent):
        self.parent = parent
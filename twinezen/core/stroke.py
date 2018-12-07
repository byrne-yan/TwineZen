from .basics import *

class Stroke():
    def __init__(self,direction,kseries):
        self.level = kseries[0].level
        self.direction = direction
        self.k_from = kseries[0]
        self.k_to = kseries[-1]
        
    def __get_attr__(self,name):
        if name == "top":
            getattr(self,name,self.direction==Direction.DOWN?self.k_from:self.k_to)
        elif name == "bottom":
            getattr(self,name,self.direction==Direction.DOWN?self.k_to:self.k_from)
        

def split_stroke(kseries)
    stroke = Stroke(kseries.level)
    return [stroke]

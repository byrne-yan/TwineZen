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
        
    def split_stroke(kseries,prevStroke=None)
        if prevStroke is None:'identify first direction
            pass

        if prevStroke.direction == Direction.UP:
            return Stroke.split_stroke_up(kseries,prevStroke)
        else:
            return Stroke.split_stroke_down(kseries,prevStroke)

    def identify_first_stroke(kseries):
        'looking for first 
        
    def split_stroke_up(kseries,prevStroke):
        pass
    
    def split_stroke_down(kseries,prevStroke):
        pass    

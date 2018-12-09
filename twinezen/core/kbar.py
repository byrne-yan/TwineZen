from .basics import *

class KBar():
    def __init__(self,no,time,open_price,close_price,top_price,bottom_price,volume,level, includes = None):
        self.no = no
        self.time = time
        self.open = open_price
        self.close = close_price
        self.top = top_price
        self.bottom = bottom_price
        self.volume = volume
        self.level = level
        self.includes = includes
##        self.boll = {upper:0,middle:0,lower:0}
##        self.macd = {macd:0,diff:0,dea:0}
##        sell.average = {five:0,ten:0,twenty:0,thirty:0,sixty:0,half_year:0,year:0}        
    def __get_attr__(self,name):
        if name == "top":
            getattr(self,name,self.k_from if self.direction==Direction.DOWN else self.k_to)
        elif name == "bottom":
            getattr(self,name,self.k_to if self.direction==Direction.DOWN else self.k_from)
            
    def __repr__(self):
        return '%sK(%r,lvl=%r, t=%r, top=%r, bottom=%r)' % \
               ('M' if self.isMerged() else '',self.no, self.level, self.time, self.top, self.bottom)
        
    def includedBy(self,k2):
        return k2.top >= self.top and k2.bottom <=self.bottom
    
    def inclusion(self,k2):
        return self.includedBy(k2) or k2.includedBy(self)

    def rise(self,k2):
        return not self.inclusion(k2) and k2.top > self.top

    def fall(self,k2):
        return not self.inclusion(k2) and k2.top < self.top

    def isMerged(self):
        return self.includes is not None and len(self.includes)>0

    def merge(self,k2,direction):
        return merge_k(self,k2,direction)
    
def merge_k(k1,k2,direction):
    assert(direction==Direction.UP or direction==Direction.DOWN)
    assert(k1.level==k2.level)
    assert( k1.inclusion(k2))

    top_price = None
    bottom_price = None
    no = None
    time = None
    if direction==Direction.UP:
        if k2.includedBy(k1):
            top_price = k1.top
            bottom_price = k2.bottom
            no = k1.no
            time = k1.time
        else:
            top_price = k2.top
            bottom_price = k1.bottom
            no = k2.no
            time = k2.time
    else:
        if k2.includedBy(k1):
            top_price = k2.top
            bottom_price = k1.bottom
            no = k1.no
            time = k1.time
        else:
            top_price = k1.top
            bottom_price = k2.bottom
            no = k2.no
            time = k2.time
            
        
    includes = (k1.includes if k1.isMerged() else [k1]) +\
        (k2.includes if k2.isMerged() else [k2])

    return KBar(no,time,k1.open,k2.close,top_price,bottom_price,k1.volume+k2.volume,k1.level,includes)

##def determine_peak(kseries):
##    prev = kseries[0]
##    for i in range(1,len(kseries)-1):
##        if not prev.inclusion(kseries[i]) and not k.inclusion(keseries[i+1]):
##            return Peak(prev,kseries[i]，kseries[i+1])
                        
        

from abc import ABCMeta
from .basics import *

class TrackType(Enum):
    UNKNOWN = 0
    RISE = 1
    FALL = 2
    PLATFROM = 3

"""
lowest track is a Segment
"""
class Track(metaclass=ABCMeta):
    
    def __init__(self,):
        self.level = Level.L_UNKNOWN
        self.direction = Direction.UNKNOWN
        self.intepretation = None
        self.type = TrackType.UNKNOWN
        self.subtracks = []

    def isComplete(self):
        if self.intepretation is None:
            self.analyze()
            
        return self.intepretation and len(self.intepretation[0].twines)>0

    def analyze(self):
        self.interpretation = [TrackInterpretation(self.subtracks)]
   
    def type(self):
        if self.intepretation is None or len(self.intepretation[0].twines)==0:
            return TrackType.UNKNOWN           
        elif len(self.intepretation[0].twines)>1:
            return TrackType.FALL if self.intepretation[0].twines[0].ZG > self.intepretation[0].twines[1].ZG else TrackType.RISE
        elif len(self.intepretation[0].twines)==1:
            return TrackType.PLATFORM

    def decompostion(self):
        return []
        
class TrackInterpretation():
    def __init__(self,tracks):
        self.tracks = tracks
        self.twines = []

        

    def twine_list(self):
        return self.twines
    
        
    def __repr__(self):
        pass
        
from .segment import Segment
Track.register(Segment)

    

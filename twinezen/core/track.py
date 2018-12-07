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
    def __init__(self):
        self.level = Level.L_UNKNOWN
        self.direction = Direction.UNKNOWN
        self.type = TrackType.UNKNOWN

    def isComplete(self):
        pass

    def analyze(self):
        return []

class TrackInterpretation():
    def __init__(self):
        self.tracks = tracks
        
    def __repr__(self):
        
        
from .segment import Segment
Track.register(Segment)

    

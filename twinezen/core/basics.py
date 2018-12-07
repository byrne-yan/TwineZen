from enum import Enum
class Level(Enum):
    L_UNKNOWN = 0
    L_1M = 1
    L_5M = 2
    L_30M = 3 
    L_DAY = 4
    L_WEEK = 5
    L_MONTH = 6
    L_SEASON = 7
    L_YEAR = 8

class Direction(Enum):
    UNKNOWN = 0
    UP = 1
    DOWN = 2

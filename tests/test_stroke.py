from twinezen.core import Level
from twinezen.core import KBar
from twinezen.core import Stroke

class TestStroke():
    def test_create(self):
        kseries = [
            KBar(0,"20181209",1,2,2.5,0.5,1000,Level.L_DAY)
            ]
        
class TestStrokeSplit():
    def test_first_stroke(self):
        kseries = [
            KBar(0,"20181209",1,3,3,1,1000,Level.L_DAY),
            KBar(1,"20181210",2,4,4,2,1000,Level.L_DAY),
            KBar(2,"20181211",3,5,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,6,6,4,1000,Level.L_DAY),
            KBar(4,"20181213",5,7,7,5,1000,Level.L_DAY),
            KBar(5,"20181214",4,6,6,4,1000,Level.L_DAY)
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(strokes and len(strokes)>0)
        

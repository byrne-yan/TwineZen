from twinezen.core import Level
from twinezen.core import KBar
from twinezen.core import Stroke
from twinezen.core import Direction
import pytest

class TestStroke():
    def test_create(self):
        kseries = [
            KBar(0,"20181209",1,2,2.5,0.5,1000,Level.L_DAY)
            ]

class TestStrokeSplit():
##    @pytest.mark.skip
    def test_first_stroke_strait_rise(self):
        kseries = [
            KBar(0,"20181209",1,3,3,1,1000,Level.L_DAY),
            KBar(1,"20181210",2,4,4,2,1000,Level.L_DAY),
            KBar(2,"20181211",3,5,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,6,6,4,1000,Level.L_DAY),
            KBar(4,"20181213",5,7,7,5,1000,Level.L_DAY),
            KBar(5,"20181214",4,6,6,4,1000,Level.L_DAY)
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(strokes and len(strokes)==1 and strokes[0].direction == Direction.UP)
        assert(strokes[0].k_from.no == 0 and strokes[0].k_to.no == 4)
        assert(strokes[0].lowest == 1 and strokes[0].highest == 7)

##    @pytest.mark.skip        
    def test_first_stroke_rise_broken(self):
        kseries = [
            KBar(0,"20181209",1,3,3,1,1000,Level.L_DAY),
            KBar(1,"20181210",2,4,4,2,1000,Level.L_DAY),
            KBar(2,"20181211",3,5,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,6,6,4,1000,Level.L_DAY),
            KBar(4,"20181213",5,7,7,5,1000,Level.L_DAY),
            KBar(5,"20181214",4,0.8,4,0.8,1000,Level.L_DAY),
            KBar(6,"20181215",3,0.7,3,0.7,1000,Level.L_DAY),
            KBar(7,"20181216",2,0.6,2,0.6,1000,Level.L_DAY),
            KBar(8,"20181217",1,0.5,1,0.5,1000,Level.L_DAY),
            KBar(9,"20181218",0.6,2,2,0.6,1000,Level.L_DAY)
            
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(strokes and len(strokes)==1 and strokes[0].direction == Direction.DOWN)
        assert(strokes[0].k_from.no == 4 and strokes[0].k_to.no == 8)
        assert(strokes[0].lowest == 0.5 and strokes[0].highest == 7)

    def test_first_stroke_rise_broken_2(self):
        kseries = [
            KBar(0,"20181209",1,3,3,1,1000,Level.L_DAY),
            KBar(1,"20181210",2,4,4,2,1000,Level.L_DAY),
            KBar(2,"20181211",3,5,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,6,6,4,1000,Level.L_DAY),
            KBar(4,"20181213",5,7,7,5,1000,Level.L_DAY),
            KBar(5,"20181214",8,0.8,8,0.8,1000,Level.L_DAY),
            KBar(6,"20181215",3,0.7,3,0.7,1000,Level.L_DAY),
            KBar(7,"20181216",2,0.6,2,0.6,1000,Level.L_DAY),
            KBar(8,"20181217",1,0.5,1,0.5,1000,Level.L_DAY),
            KBar(9,"20181218",0.6,2,2,0.6,1000,Level.L_DAY)
            
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(len(strokes)==0)

    def test_first_stroke_rise_broken_3(self):
        kseries = [
            KBar(0,"20181209",1,3,3,1,1000,Level.L_DAY),
            KBar(1,"20181210",2,4,4,2,1000,Level.L_DAY),
            KBar(2,"20181211",3,5,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,6,6,4,1000,Level.L_DAY),
            KBar(4,"20181213",5,7,7,5,1000,Level.L_DAY),
            KBar(5,"20181214",8,0.8,8,0.8,1000,Level.L_DAY),
            KBar(6,"20181215",3,0.7,3,0.7,1000,Level.L_DAY),
            KBar(7,"20181216",2,0.6,2,0.6,1000,Level.L_DAY),
            KBar(8,"20181217",1,0.5,1,0.5,1000,Level.L_DAY),
            KBar(9,"20181218",0.8,0.4,0.8,0.4,1000,Level.L_DAY),
            KBar(10,"20181219",0.6,2,2,0.6,1000,Level.L_DAY)
            
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(len(strokes)==1 and strokes[0].direction == Direction.DOWN)
        assert(strokes[0].k_from.no == 5 and strokes[0].k_to.no == 9)
        assert(strokes[0].lowest == 0.4 and strokes[0].highest == 8)

    def test_first_stroke_rise_leftinclusion(self):
        kseries = [
            KBar(0,"20181209",1,3,3,1,1000,Level.L_DAY),
            KBar(1,"20181210",2,4,4,2,1000,Level.L_DAY),
            KBar(2,"20181211",3,5,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,6,6,4,1000,Level.L_DAY),
            KBar(4,"20181213",5,7,7,5,1000,Level.L_DAY),
            KBar(5,"20181214",5.5,6,6,5.5,1000,Level.L_DAY),
            KBar(6,"20181215",3,5,5,3,1000,Level.L_DAY)
            
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(len(strokes)==1 and strokes[0].direction == Direction.UP)
        assert(strokes[0].k_from.no == 0 and strokes[0].k_to.no == 4)
        assert(strokes[0].lowest == 1 and strokes[0].highest == 7)
        assert(strokes[0].kseries[-1].bottom == 5.5)
##    @pytest.mark.skip
    def test_first_stroke_strait_fall(self):
        kseries = [
            KBar(0,"20181209",7,5,7,5,1000,Level.L_DAY),
            KBar(1,"20181210",6,4,6,4,1000,Level.L_DAY),
            KBar(2,"20181211",5,3,5,3,1000,Level.L_DAY),
            KBar(3,"20181212",4,2,4,2,1000,Level.L_DAY),
            KBar(4,"20181213",3,1,3,1,1000,Level.L_DAY),
            KBar(5,"20181214",4,2,4,2,1000,Level.L_DAY)
            ]
        strokes = Stroke.split_stroke(kseries)
        assert(strokes and len(strokes)==1 and strokes[0].direction == Direction.DOWN)
        assert(strokes[0].k_from.no == 0 and strokes[0].k_to.no == 4)
        assert(strokes[0].lowest == 1 and strokes[0].highest == 7)

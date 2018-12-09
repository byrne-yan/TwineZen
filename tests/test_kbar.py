from twinezen.core import Level
from twinezen.core import Direction
from twinezen.core import KBar

class TestKBar():
    def test_inclued_by(self):
        k1 = KBar(0,"20181209",1,2,2.5,0.5,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.4,4,4,0.4,1000,Level.L_DAY)
        assert( k1.includedBy(k2))
        assert(not k2.includedBy(k1))
        assert(k1.inclusion(k2) and k2.inclusion(k1))

    def test_rise_and_fall(self):
        k1 = KBar(0,"20181209",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",1,3,3,1,1000,Level.L_DAY)
        assert( k1.rise(k2))
        assert( k2.fall(k1))

    def test_merge_0(self):
        k1 = KBar(0,"20181209",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        assert(not k1.isMerged())

    def test_merge_up_1(self):
        k1 = KBar(0,"20181209",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.4,3,3,0.4,1000,Level.L_DAY)

        k3 = k1.merge(k2,Direction.UP)
        assert(k3.isMerged())
        assert(k3.top==k2.top and k3.bottom==k1.bottom)
        assert(k3.no == k2.no and k3.time == k2.time)

    def test_merge_up_2(self):
        k1 = KBar(0,"20181209",0.4,3,3,0.4,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.5,2.5,2.5,0.5,1000,Level.L_DAY)

        k3 = k1.merge(k2,Direction.UP)
        assert(k3.isMerged())
        assert(k3.top==k1.top and k3.bottom==k2.bottom)
        assert(k3.no == k1.no and k3.time == k1.time)
    def test_merge_up_3(self):
        k1 = KBar(0,"20181209",0.4,3,3,0.4,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        k3 = KBar(2,"20181211",0.6,2.3,2.3,0.6,1000,Level.L_DAY)

        k4 = k1.merge(k2,Direction.UP).merge(k3,Direction.UP)
        assert(k4.isMerged())
        assert(k4.top==k1.top and k4.bottom==k3.bottom)
        assert(k4.no == k1.no and k4.time == k1.time)

    def test_merge_up_4(self):
        k1 = KBar(0,"20181209",0.4,3,3,0.4,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        k3 = KBar(2,"20181211",0.3,4,4,0.3,1000,Level.L_DAY)

        k4 = k1.merge(k2,Direction.UP).merge(k3,Direction.UP)
        assert(k4.isMerged())
        assert(k4.top==k3.top and k4.bottom==k2.bottom)
        assert(k4.no == k3.no and k4.time == k3.time)
        
    def test_merge_down_1(self):
        k1 = KBar(0,"20181209",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.4,3,3,0.4,1000,Level.L_DAY)

        k3 = k1.merge(k2,Direction.DOWN)
        assert(k3.isMerged())
        assert(k3.top==k1.top and k3.bottom==k2.bottom)
        assert(k3.no == k2.no and k3.time == k2.time)

    def test_merge_down_2(self):
        k1 = KBar(0,"20181209",0.4,3,3,0.4,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.5,2.5,2.5,0.5,1000,Level.L_DAY)

        k3 = k1.merge(k2,Direction.DOWN)
        assert(k3.isMerged())
        assert(k3.top==k2.top and k3.bottom==k1.bottom)
        assert(k3.no == k1.no and k3.time == k1.time)

    def test_merge_down_3(self):
        k1 = KBar(0,"20181209",0.4,3,3,0.4,1000,Level.L_DAY)
        k2 = KBar(1,"20181210",0.5,2.5,2.5,0.5,1000,Level.L_DAY)
        k3 = KBar(2,"20181211",0.6,2.3,2.3,0.6,1000,Level.L_DAY)
        
        k4 = k1.merge(k2,Direction.DOWN).merge(k3,Direction.DOWN)
        
        assert(k4.isMerged())
        assert(k4.top==k3.top and k4.bottom==k1.bottom)
        assert(k4.no == k1.no and k4.time == k1.time)
    
        

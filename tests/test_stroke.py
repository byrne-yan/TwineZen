from .basics import *
from .stroke import Stroke

class TestStroke():
    def test_create(self):
        kseries = [
            KBar(0,"20181209",1,2,2.5,0.5,1000,Level.L_DAY)
            ]

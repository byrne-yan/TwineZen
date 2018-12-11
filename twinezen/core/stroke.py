from .basics import *
from fysom import Fysom

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
        fsm = Fysom(
                { 'initial': 'start',
                  'events': [
                      {'five_rise_k','start','up_g'},
                      {'left_inclusion','up_g','up_g'},
                      {'fall_k','up_g','up_0_0'},
                      {'left_inclusion','up_0_0','up_0_0'},
                      {'other_k','up_0_0','up_c_0'},
                      {'left_inclusion','up_c_0','up_c_0'},
                      {'other_k','up_c_0','up_c_p1'},
                      {'left_inclusion','up_c_p1','up_c_p1'},
                      {'other_k','up_c_p1','up_c_p1'},
                      {'lower_fall_k','up_c_p1','up_c_p2'},
                      {'left_inclusion','up_c_p2','up_c_p2'},
                      {'lower_fall_k','up_c_p2','up_c_p2'},
                      {'left_inclusion','up_c_p2','down_g'},                      
                      {'higher_peak',['up_0_0','up_c_0','up_c_p1','up_c_p2','up_g'],'up_g'},

                      {'five_fall_k','start','down_g'},
                      {'left_inclusion','down_g','down_g'},
                      {'rise_k','down_g','down_0_0'},
                      {'left_inclusion','down_0_0','down_0_0'},
                      {'other_k','down_0_0','down_c_0'},
                      {'left_inclusion','down_c_0','down_c_0'},
                      {'other_k','down_c_0','down_c_p1'},
                      {'left_inclusion','down_c_p1','down_c_p1'},
                      {'other_k','down_c_p1','down_c_p1'},
                      {'higher_rise_k','down_c_p1','down_c_p2'},
                      {'left_inclusion','down_c_p2','down_c_p2'},
                      {'higher_rise_k','down_c_p2','down_c_p2'},
                      {'left_inclusion','down_c_p2','down_g'},                      
                      {'lower_peak',['down_0_0','down_c_0','down_c_p1','down_c_p2','down_g'],'down_g'}
                      ],
                  'callbacks':{
 
                     }
                  })


        fiveK = getFiveMonoK(kseries)
        if fiveK is None:
            return []
        if fiveK.direction == Direction.UP:
            fsm.five_rise_k(kseries[fiveK.begin:fiveK.end])
            assert(fsm.current == 'up_g')
        else:
            fsm.five_fall_k(kseries[fiveK.begin:fiveK.end])
            assert(fsm.current == 'down_g')
                
        for i in range(fiveK.end,len(kseries)):
            ck = kseries[i]
            if ck.includedBy(fsm.lastK):
                fsm.left_inclusion(k=ck)

            elif fsm.prevStroke and fsm.prevStroke.direction==Direction.UP:
                if ck.top > sfm.prevStroke.top:
                    fsm.higher_peak(k=ck)
                elif fsm.lastK.fall(ck):
                    fsm.fall_k(k=ck)
                elif fsm.lastK.rise(ck):
                    fsm.rise_k(k=ck)
                

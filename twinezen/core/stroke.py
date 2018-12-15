from .basics import *
from fysom import Fysom

class StrokeMaker():
    def __init__(self,k):
        self.kseries = [k]
        self.direction = Direction.UNKNOWN
        self.highest = k.top
        self.lowest = k.bottom
        self.peak = 0
        self.complete = False
        
    def is_up(self):
        return self.direction == Direction.UP
    def is_down(self):
        return self.direction == Direction.DOWN
    
    def lastK(self):
        return self.kseries[-1]

    def __str__(self):
        dirSymbol = '↑' if self.direction==Direction.UP else ( '↓' if self.direction==Direction.DOWN else '↕')
        return '%s[%s,%s]@%s%s%s%r' % (len(self.kseries),self.lowest,self.highest,self.peak,dirSymbol,'●' if self.complete else '○',self.kseries)
    def to_stroke(self):
        if not self.complete:
            return None
        return Stroke(self.direction,self.kseries)

        
class Stroke():
    def __init__(self,direction,kseries):
        self.kseries = kseries
        self.level = kseries[0].level
        self.direction = direction
        self.k_from = kseries[0]
        self.k_to = kseries[-1]
        self.lowest = kseries[0 if direction==Direction.UP else -1].bottom
        self.highest = kseries[-1 if direction==Direction.UP else 0].top
        
    def __get_attr__(self,name):
        if name == "top":
            getattr(self,name,self.k_from if self.direction==Direction.DOWN else self.k_to)
        elif name == "bottom":
            getattr(self,name,self.k_to if self.direction==Direction.DOWN else self.k_from)
    def getFirstStroke(kseries):
        def on_ud1(e):
            if hasattr(e.fsm,'stroke') and not e.fsm.stroke.kseries[e.fsm.stroke.peak].includedBy(e.args[0]):
                stroke = StrokeMaker(e.fsm.stroke.kseries[e.fsm.stroke.peak])
                stroke.backHops = len(e.fsm.stroke.kseries)-e.fsm.stroke.peak
##                print('stroke.backHops:%s' % stroke.backHops)
                e.fsm.stroke = stroke
            else:
                e.fsm.stroke = StrokeMaker(e.args[0])

        def on_u1(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            s.highest = k.top
            s.peak = len(s.kseries)-1
            s.direction = Direction.UP

        def on_u2(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            if e.event == 'rise_k':
                s.highest = k.top
                s.peak = len(s.kseries)-1

        def on_u3(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            if e.event == 'rise_k':
                s.highest = k.top
                s.peak = len(s.kseries)-1

        def on_u4(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            s.highest = k.top
            s.peak = len(s.kseries)-1

        def on_u5(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.complete = True
            
        def on_d1(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            s.lowest = k.bottom
            s.peak = len(s.kseries)-1
            s.direction = Direction.DOWN

        def on_d2_3(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            if e.event == 'fall_k':
                s.lowest = k.bottom
                s.peak = len(s.kseries)-1

        def on_d2_3(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            if e.event == 'fall_k':
                s.lowest = k.bottom
                s.peak = len(s.kseries)-1

        def on_d4(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries.append(k)
            s.lowest = k.bottom
            s.peak = len(s.kseries)-1

        def on_d5(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.complete = True

        def on_reenter(e):
            k =e.args[0]
            s = e.fsm.stroke
            s.kseries[-1] = s.kseries[-1].merge(k,s.direction)
            
        def genEvent(fsm,k):
            print(k)
            if fsm.current == 'start':
                return 'any_k'

            if k.includedBy(fsm.stroke.lastK()):
                return 'left_inclusion'
            elif fsm.stroke.lastK().rise(k):
                if not fsm.stroke.is_down():
                    if k.top > fsm.stroke.highest:
                        return 'rise_k'
                    else:
                        return 'fluctuate_k'
                else:
                    if k.top > fsm.stroke.highest:
                        return 'stroke_broken'
                    else:
                        return 'fluctuate_k'                
            elif fsm.stroke.lastK().fall(k):
                if not fsm.stroke.is_up():
                    if k.bottom < fsm.stroke.lowest:
                        return 'fall_k'
                    else:
                        return 'fluctuate_k'
                else:
                    if k.bottom < fsm.stroke.lowest:
                        return 'stroke_broken'
                    else:
                        return 'fluctuate_k'                    
            else:
                if (fsm.stroke.is_up() and k.bottom < fsm.stroke.lowest) or \
                   (fsm.stroke.is_down() and k.top < fsm.stroke.highest):
                    return 'stroke_broken'
                else:
                    return 'right_inclusion'

        fsm = Fysom({'initial':'start',
                    'events':[
                        {'name':'any_k','src':'start','dst':'ud1'},
                        {'name':'rise_k','src':'ud1','dst':'u1'},
                        {'name':'fall_k','src':'ud1','dst':'d1'},
##                        {'name':'left_inclusion','src':'ud1','dst':'ud1'},
                        {'name':'right_inclusion','src':'ud1','dst':'ud1'},
                        {'name':'rise_k','src':'u1','dst':'u2'},
                        {'name':'fluctuate_k','src':'u1','dst':'u2'},
                        {'name':'rise_k','src':'u2','dst':'u3'},
                        {'name':'fluctuate_k','src':'u2','dst':'u3'},
                        {'name':'rise_k','src':'u3','dst':'u4'},
                        {'name':'fluctuate_k','src':'u3','dst':'u4'},
                        {'name':'fluctuate_k','src':'u4','dst':'u5'},

                        {'name':'fall_k','src':'d1','dst':'d2'},
                        {'name':'fluctuate_k','src':'d1','dst':'d2'},
                        {'name':'fall_k','src':'d2','dst':'d3'},
                        {'name':'fluctuate_k','src':'d2','dst':'d3'},
                        {'name':'fall_k','src':'d3','dst':'d4'},
                        {'name':'fluctuate_k','src':'d3','dst':'d4'},
                        {'name':'fluctuate_k','src':'d4','dst':'d5'},

                        {'name':'stroke_broken','src':['u1','u2','u3','u4','d1','d2','d3','d4'],'dst':'ud1'},
                        {'name':'left_inclusion','src':'ud1','dst':'ud1'},
                        {'name':'left_inclusion','src':'u1','dst':'u1'},
                        {'name':'left_inclusion','src':'u2','dst':'u2'},
                        {'name':'left_inclusion','src':'u3','dst':'u3'},
                        {'name':'left_inclusion','src':'u4','dst':'u4'},
                        {'name':'left_inclusion','src':'d1','dst':'d1'},
                        {'name':'left_inclusion','src':'d2','dst':'d2'},
                        {'name':'left_inclusion','src':'d3','dst':'d3'},
                        {'name':'left_inclusion','src':'d4','dst':'d4'}
                        
                        ],
                    'callbacks':{
                        'onud1':on_ud1,
                        'onu1':on_u1,
                        'onu2':on_u2,
                        'onu3':on_u3,
                        'onu4':on_u4,
                        'onu5':on_u5,
                        'ond1':on_d1,
                        'ond2':on_d2_3,
                        'ond3':on_d2_3,
                        'ond4':on_d4,
                        'ond5':on_d5,
                        'onreenteru1':on_reenter,
                        'onreenteru2':on_reenter,
                        'onreenteru3':on_reenter,
                        'onreenteru4':on_reenter,
                        'onreenterd1':on_reenter,
                        'onreenterd2':on_reenter,
                        'onreenterd3':on_reenter,
                        'onreenterd4':on_reenter
                        }
                     }
                    )
        def printstatechange(e):
            print('event: %s, src: %s, dst: %s,status:%s' % (e.event, e.src, e.dst,e.fsm.stroke))

        fsm.onchangestate = printstatechange
        
        assert(fsm.current=='start')
        e = genEvent(fsm,kseries[0])
        fsm.trigger(e,kseries[0])            
        i = 1
        while  i < len(kseries):
            k = kseries[i]
            if hasattr(fsm.stroke,'backHops'):
                delattr(fsm.stroke,'backHops')
##            print("K:%s" % k)
            e = genEvent(fsm,k)
            fsm.trigger(e,k)            
            if fsm.current=='d5' or fsm.current=='u5' :
                print('Finished')
                return fsm.stroke.to_stroke()
            i =  i - getattr(fsm.stroke,'backHops',0) + 1
        return

            

                    
    def split_stroke(kseries):
##        fsm = Fysom(
##                { 'initial': 'start',
##                  'events': [
##                      {'five_rise_k','start','up_g'},
##                      {'left_inclusion','up_g','up_g'},
##                      {'fall_k','up_g','up_0_0'},
##                      {'left_inclusion','up_0_0','up_0_0'},
##                      {'other_k','up_0_0','up_c_0'},
##                      {'left_inclusion','up_c_0','up_c_0'},
##                      {'other_k','up_c_0','up_c_p1'},
##                      {'left_inclusion','up_c_p1','up_c_p1'},
##                      {'other_k','up_c_p1','up_c_p1'},
##                      {'lower_fall_k','up_c_p1','up_c_p2'},
##                      {'left_inclusion','up_c_p2','up_c_p2'},
##                      {'lower_fall_k','up_c_p2','up_c_p2'},
##                      {'left_inclusion','up_c_p2','down_g'},                      
##                      {'higher_peak',['up_0_0','up_c_0','up_c_p1','up_c_p2','up_g'],'up_g'},
##
##                      {'five_fall_k','start','down_g'},
##                      {'left_inclusion','down_g','down_g'},
##                      {'rise_k','down_g','down_0_0'},
##                      {'left_inclusion','down_0_0','down_0_0'},
##                      {'other_k','down_0_0','down_c_0'},
##                      {'left_inclusion','down_c_0','down_c_0'},
##                      {'other_k','down_c_0','down_c_p1'},
##                      {'left_inclusion','down_c_p1','down_c_p1'},
##                      {'other_k','down_c_p1','down_c_p1'},
##                      {'higher_rise_k','down_c_p1','down_c_p2'},
##                      {'left_inclusion','down_c_p2','down_c_p2'},
##                      {'higher_rise_k','down_c_p2','down_c_p2'},
##                      {'left_inclusion','down_c_p2','down_g'},                      
##                      {'lower_peak',['down_0_0','down_c_0','down_c_p1','down_c_p2','down_g'],'down_g'}
##                      ],
##                  'callbacks':{
## 
##                     }
##                  })


        firstStroke = Stroke.getFirstStroke(kseries)
##        if fiveK is None:
##            return []
##        if fiveK.direction == Direction.UP:
##            fsm.five_rise_k(kseries[fiveK.begin:fiveK.end])
##            assert(fsm.current == 'up_g')
##        else:
##            fsm.five_fall_k(kseries[fiveK.begin:fiveK.end])
##            assert(fsm.current == 'down_g')
##                
##        for i in range(fiveK.end,len(kseries)):
##            ck = kseries[i]
##            if ck.includedBy(fsm.lastK):
##                fsm.left_inclusion(k=ck)
##
##            elif fsm.prevStroke and fsm.prevStroke.direction==Direction.UP:
##                if ck.top > sfm.prevStroke.top:
##                    fsm.higher_peak(k=ck)
##                elif fsm.lastK.fall(ck):
##                    fsm.fall_k(k=ck)
##                elif fsm.lastK.rise(ck):
##                    fsm.rise_k(k=ck)
##                
        return [firstStroke] if firstStroke is not None else []
                



import Track
class TwineSection()
    def __init__(self,track1,track2,track3):
        #check level of tracks
        if track1.level == track2.level and track2.level == track3.level
            self.level = track1.level
            self.tracks = [track1,track2,track3]
        else:
            raise Exception('Tracks are not same level!')
        
        
    def __repr__(self):
        'Twine(level=%r, (%r, fragment=%r), (nofollow=%r,nofollow=%r))' % \
(self.level, self.timerange, self.fragment, self.nofollow)
        
            

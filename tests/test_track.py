# -*- coding: utf-8 -*-

import pytest

from twinezen.core import * 
from twinezen.core import Segment
from twinezen.core import Track


class TestTrack():
    """Basic test cases."""

    def test_segment_isa_track(self):
        segment = Segment()
        assert isinstance(segment,Track)

    def test_level(self):
        track = Track()
        assert track.level == Level.L_UNKNOWN
        
    def test_direction(self):
        track = Track()
        assert track.direction == Direction.UNKNOWN

    def test_complete_1(self):
        track = Track()
        assert not track.isComplete()

    def test_complete_2(self):
        track = Track()
        assert not track.isComplete()

    def test_exists_twinesection(self):
        pass
        
        

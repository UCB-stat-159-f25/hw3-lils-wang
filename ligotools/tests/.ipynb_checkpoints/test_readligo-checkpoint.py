from ligotools import readligo as rl
import numpy as np
import pytest

def test_segmentlist():
    segments = [[123, 456], [789, 123]]
    rl_segments = rl.SegmentList(segments)
    assert list(rl_segments) == segments

def test_dq2segs():
    dq = np.array([0, 0, 0, 1, 1, 0, 1, 1, 0])
    gps_start = 100
    test = rl.dq2segs(dq, gps_start)
    expected = [(103, 105), (106, 108)]
    assert list(test) == expected
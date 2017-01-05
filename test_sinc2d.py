from sinc2d import *
import numpy as np

def test_sinc2d_corner():
    x, y = 0, 0
    expect = 1
    calc = sinc2d(x,y)
    assert calc == expect

def test_sinc2d_x0():
    x, y = 0, 0.6
    expect = np.sin(y)/y
    calc = sinc2d(x,y)
    assert calc == expect

def test_sinc2d_y0():
    x, y = 0.6, 0
    expect = np.sin(x)/x
    calc = sinc2d(x,y)
    assert calc == expect



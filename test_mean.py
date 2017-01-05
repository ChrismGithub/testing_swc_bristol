# if there is any function called mean.py, import it
from mean import *

def test_ints():
    """Test that mean function works, mean of [1,2,3,4,5] should be 3"""
    input = [1,2,3,4,5]
    calc_value = mean(input)
    expect_value = 3
    assert calc_value == expect_value

#def test_empty():
#    """Test for empty list error message"""
#    input = []
#    error_msg = mean(input)
#    assert error_msg == "Please provide a list of numbers."

def test_float():
    """Test that floating numbers work"""
    calc_value=mean([1.0,2.0,3.0,4.0])
    expect = 2.5
    assert expect == calc_value

def test_one():
    calc=mean([2.3])
    expect=2.3
    assert expect == calc

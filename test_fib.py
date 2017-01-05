from fib import *

def test_fib0():
    expect = 1
    calc = fib(0)
    assert calc == expect

def test_fib1():
    expect = 1
    calc = fib(1)
    assert calc == expect

def test_fib3():
    expect = 3
    calc = fib(3)
    assert calc == expect

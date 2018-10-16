from operator import add, mul
from functools import reduce

def xsum(*args):
    return reduce(add, args)

def xmult(*args):
    return reduce(mul, args)

def square(a):
    return a * a

def cube(a):
    return a ** 3    
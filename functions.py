from operator import add
from functools import reduce

def xsum(*args):
    return reduce(add, args)

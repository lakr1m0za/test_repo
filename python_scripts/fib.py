from math import *

def fib(n):
    y = ((1+sqrt(5))/2)
    f = (y**n/sqrt(5))
    return (round(f))
    
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(5) == 5
    assert fib(9) == 34
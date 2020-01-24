def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def sfactorial (k):
    i = 0
    l = 1
    while i <= k:
        l = l * int(factorial(i))
        i = i + 1
    return (factorial(k), l)    
    
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sfactorial(0) == (1, 1)
    assert sfactorial(1) == (1, 1)
    assert sfactorial(2) == (2, 2)
    assert sfactorial(3) == (6, 12)
    assert sfactorial(4) == (24, 288)
    assert sfactorial(5) == (120, 34560)
def dfactorial (n):
    if n == 0:
        return 1
    elif n < 0:
        return 1
    else:
        return n * dfactorial(n - 2)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert dfactorial(0) == 1
    assert dfactorial(1) == 1
    assert dfactorial(2) == 2
    assert dfactorial(3) == 3
    assert dfactorial(4) == 8
    assert dfactorial(5) == 15

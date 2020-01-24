def kfactorial (n, k = 1):
    if n == 0:
        return 1
    elif n < 0:
        return 1
    else:
        return n * kfactorial(n - k, k)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert kfactorial(0) == 1
    assert kfactorial(1, 10) == 1
    assert kfactorial(10, 1) == 3628800
    assert kfactorial(8, 3) == 80
    assert kfactorial(8) == 40320
    assert kfactorial(6, 3) == 18


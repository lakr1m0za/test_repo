def sum5not3(n):
    res = 0
    while n > 0:
        if (n % 5 == 0) and (n % 3 != 0):
            res += n
        n -= 1
    return (res)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum5not3(100) == 735
    assert sum5not3(422) == 11760

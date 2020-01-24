def maxId (L):
    for x in L:
        if type(x) != int:
            i = L.index(x)
            L.pop(i)
            L.insert(i, int(x))
    return (L.index(max(L)))

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert maxId([1, 2, '42', '3', '4', '5', 6, 13]) == 2
    assert maxId(['0', 1, 2, '3', '4', '5', 6, '666', 42]) == 7
    assert maxId([999]) == 0

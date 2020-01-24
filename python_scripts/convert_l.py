def convert (L):
    for x in L:
        if type(x) != int:
            i = L.index(x)
            L.pop(i)
            L.insert(i, int(x))
    return (L)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert convert([1, 2, '3', '4', '5', 6]) == [1, 2, 3, 4, 5, 6]

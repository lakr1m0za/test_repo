def common(list_a, list_b):
    list_c = []
    for x in list_a:
        if x in list_b:
            list_c.append(x)
    return (list_c)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert common([0, 2, 3, 4, 5, 19, 42], [0, 6, 19, 33, 42, 55, 66, 77, 99, 101, 256]) == [0, 42, 19]

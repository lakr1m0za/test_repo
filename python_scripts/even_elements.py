def even_elements(l):
    j = []
    for x in l:
        if x % 2 == 0:
            j.append(x)
    return (j)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert even_elements( [1, 1, 2, 3, 5, 8, 13, 21, 34]) == [2, 8, 34]


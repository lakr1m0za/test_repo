def last_to_first(l):
    return (l[::-1])

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert last_to_first( [1, 1, 2, 3, 5, 8, 13, 21, 34]) == [34, 21, 13, 8, 5, 3, 2, 1, 1]



#def even_indeces(l):
#    x = 0
#    j = []
#    while x < len(l):
#        if x % 2 == 0:
#            j.append(l[x])
#        x += 1
#    return (j)


def even_indeces(l):
    return l[::2]

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert even_indeces( [1, 1, 2, 3, 5, 8, 13, 21, 34]) == [1, 2, 5, 13, 34]

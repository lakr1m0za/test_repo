def index_diff_1(l):
    i = 0
    while i < (len(l)-1):
        if abs(l[i] - l[i+1]) == 1:
            index = i
            return index
        else:
            i += 1

def index_diff_2(l):
    for i in l:
        ind = l.index(i)
        if abs(l[ind] - l[ind+1]) == 1:
            index = ind
            return index


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert index_diff_1([1, 4, 67, 4, 2, 65, 66]) == 5
    assert index_diff_1([1, 2, 6]) == 0
    assert index_diff_1([1, 2]) == 0
    assert index_diff_1([1, 4, 67, 4, 6, 5, 66]) == 4
#    assert index_diff([1]) == 0

def translate (k, n = 2):
    l = ''
    while k != 0:
        l = l + str(k%n)
        k = k//n
    return (l[::-1])
        

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate(19) == '10011'
    assert translate(19, 7) == '25'
    assert translate(10, 2) == '1010'
    assert translate(8, 3) == '22'

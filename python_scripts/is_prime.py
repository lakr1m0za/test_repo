def is_prime(n):
    j = 2
    i = 1
    for i in [2, 3, 5, int(n**0.5)]:
        if n%i == 0:
            j = j + 1
            if j > 2:
                return(bool(0))
    return(bool(1))
    
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_prime(7) == True
    assert is_prime(15) == False
    assert is_prime(99) == False
    assert is_prime(103) == True

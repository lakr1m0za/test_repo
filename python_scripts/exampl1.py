def all_the_same(elements):
    i = 0
    if len(elements) == 0:
        return True
    while i < (len(elements)-1):
        if elements[i] != elements[i+1]:
            return False
        else:
            i += 1
    return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    assert all_the_same([1, 1, 2]) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

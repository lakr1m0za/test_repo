#L = input()

def sum_mass(elem):
    elem = list(map(int, elem))
    i = 0
    for x in elem:
        i = i + x
    return i

if __name__ == '__main__':
    assert sum_mass([1, 2]) == 3
    assert sum_mass([1, 2, 3]) == 6
    assert sum_mass([99, 234, 34, 1, 0, -5, 55, 666, 42]) == 1126
    print("Coding complete? Click 'Check' to earn cool rewards!")


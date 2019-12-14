def counter(T):
    count = 0
    i = 0
    unique_T = []
    l = len(T)
    for x in T:
        for f in x.lower():
            if f not in unique_T:
                count = len(x)
                unique_T.append(f)
    if len(unique_T) == count:
        while i < (l-1):
            if len(T[i]) <= len(T[i+1]):
                i += 1
            else:
                count = len(T[i+1])
                break
            count = len(T[i])
    return count
                
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert counter(['Aa', 'ABBA', 'ab', 'AaAa', 'AaAaAa']) == 4
    assert counter(['Aabcd', 'ab']) == 5
    assert counter(['A', 'AAAA']) == 4
    assert counter(['AAAaaa', 'ab']) == 2
    assert counter(['Aa', 'ab', 'AaAa', 'AaAaAa', 'ABBA']) == 4
    

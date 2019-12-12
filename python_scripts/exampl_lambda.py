def counter(T):
    return max(map(lambda s: (len(set(s.lower())), len(s)), T))[1]

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert counter(['AAAaaa', 'ab']) == 2
    assert counter(['A', 'AAAA']) == 4
    assert counter(['Aa', 'ab', 'AaAa', 'AaAaAa', 'ABBA']) == 4
    assert counter(['Aa', 'ABBA', 'AaAa', 'AaAaAa', 'ab']) == 4
    assert counter(['Aabcd', 'ab']) == 5
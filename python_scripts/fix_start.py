def fix_start(s):
    return (s[0] + s[1:].replace(s[0], '*'))

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert fix_start('babble') == 'ba**le'
    assert fix_start('aabirvalg') == 'a*birv*lg'
    assert fix_start('donut') == 'donut'
    assert fix_start('     ') == ' ****'
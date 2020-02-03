def both_ends(s):
    if len(s) < 2:
        return ('')
    return (s[:2]+s[len(s)-2:len(s)])    
    
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert both_ends('Слово') == 'Слво'
    assert both_ends('xyz') == 'xyyz'
    assert both_ends('a') == ''

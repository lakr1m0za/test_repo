def donuts(n):
    if n > 9:
        return ('Всего пончиков: много')
    else:
        return('Всего пончиков: ' + str(n))
    
if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert donuts(5) == 'Всего пончиков: 5'
    assert donuts(25) == 'Всего пончиков: много'

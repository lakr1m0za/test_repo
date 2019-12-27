if __name__ == '__main__':
    x = 2#int(input())
    y = 2#int(input())
    z = 2#int(input())
    n = 2#int(input())
    
    ar = []
    p = 0
    for i in range (x + 1 ) :
        for j in range(y + 1):
            for l in range(z + 1):
                if i+j+l != n:
                    ar.append([])
                    ar[p] = [i, j, l]
                    p += 1
    print (ar)
    
    ar = []
    p = 0
    print ([ [i, j, l] for i in range(x + 1) for j in range(y + 1) for l in range(z + 1) if ( (i + j + l) != n )])
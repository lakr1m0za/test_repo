i = int(input())
#for x in range(2, i):
#    if i%x == 0:
#        print (x)
#        break

print ([x for x in range(2, i) if i%x == 0][0])
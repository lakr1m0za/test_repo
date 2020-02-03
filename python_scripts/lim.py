#import math
#x = 0
#while x < 1000000:
#    lim = 2 * math.atan(x)
#    x = x + 1000
#print (round(lim, 3))


import math
def f(x):
    return 2 * math.atan(x)

lim = f(float('+inf'))
print (lim)
from scipy import constants
#lam = hc/(eU)
h = constants.h
c = constants.c
e = constants.e
print (h, c, e)
U = 2
lam = (h*c)/(e*U)
print (lam)
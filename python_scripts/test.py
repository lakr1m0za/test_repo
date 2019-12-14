import random
s = '{} is {} in Spain'
L = ['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve']
#1
n = random.randint(0, 9)
#2
x = L[n]
#3
print (x)
s = s.format(x, n)
print (s)
#4
a = ('2 3 2')#input()
b = ('8 1 9')#input()
a = a.split()
b = b.split()
c = 0
d = 0
for x in a:
    c = c + int(x)
for x in b:
    d = d + int(x)
print ('#'.join([str(c), str(d)]))
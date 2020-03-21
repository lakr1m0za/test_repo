t = input()
f = open(t, 'r')
s = 0
i = 0
text = f.read().split("\n")
print (text[len(text)-2])
f.close()
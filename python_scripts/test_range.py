A = ()
for i in range(0, 11):
    A[i] = i
t = A[0]
for i in range(1, 11):
    A[i - 1] = A[i]
A[10] = t
print (A)
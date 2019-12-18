i = input()

if i == 'int':
    a = int(input())
    b = int(input())
    if a == 0 and b == 0:
        print ('Empty Ints')
    else:
        print (a + b)
elif i == 'str':
    a = str(input())
    if a == "":
        print ('Empty String')
    else:
        print (a)
elif i == 'list':
    a = input()
    a = a.split()
    if a == []:
        print ('Empty List')
    else:
        print (a[-1])
else:
    print ('Unknown type')
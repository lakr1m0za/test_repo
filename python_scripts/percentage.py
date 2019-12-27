#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika

#2
#Harsh 25 26.5 28
#Anurag 26 28 30
#Harsh

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    y = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        i = student_marks[query_name]
        for x in range(len(i)):
            y += i[x]
    print ("{0:.2f}".format(float(y/3)))
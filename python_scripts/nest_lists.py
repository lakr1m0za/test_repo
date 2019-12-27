#students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
#n = 5
if __name__ == '__main__':
    students = []
    for _ in range(0, int(input())):
        students.append([input(), float(input())])
    second_lowest = sorted(list(set([score for name, score in students])))[1]
    print('\n'.join([a for a,b in sorted(students) if b == second_lowest]))
    
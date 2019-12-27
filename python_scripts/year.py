def is_leap(year):
    leap = False
    if int(year) % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        leap = True
    return leap

for year in range(1900, 100001):
    print(year, is_leap(year))
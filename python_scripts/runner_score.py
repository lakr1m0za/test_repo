if __name__ == '__main__':
    n = 5#int(input())
    arr = list(map(int, input().split()))#[2, 2, 6, 6, 5]
    i = max(arr)
    while max(arr) == i:
        arr.remove(i)
    print(max(arr))
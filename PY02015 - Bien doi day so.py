def check(arr):
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return False
    return True

while True:
    a = [int(x) for x in input().split()]
    if a[0] == a[1] == a[2] == a[3] == 0:
        break
    count = 0
    while not check(a):
        b = a[0]
        for i in range(3):
            a[i] = abs(a[i] - a[i + 1])
        a[3] = abs(a[3] - b)
        count += 1
    print(count)
t = int(input())
for i in range(t):
    arr = input().split()
    n, x, m = float(arr[0]), float(arr[1]), float(arr[2])
    s = n
    count = 0
    while(s < m):
        s = s + s*x*1/100
        count += 1
    print(count)

    
t = int(input())
for i in range(t):
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(y) for y in input().split()])
    c = 0
    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            c = 1
            break
    if c == 0:
        print("YES")
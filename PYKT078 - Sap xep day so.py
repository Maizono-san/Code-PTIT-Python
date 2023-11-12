t = int(input())
for i in range(t):
    s = input().split()
    n,m = int(s[0]), int(s[1])
    a = [int(x) for x in input().split()]
    M = max(a)
    tmp = 0
    for j in range(n):
        if a[j] == M:
            tmp = j
            break
    a.insert(j,m)
    for j in a:
        if j < 0:
            print(j,end = ' ')
    for j in a:
        if j >= 0:
            print(j,end = ' ')
    print()

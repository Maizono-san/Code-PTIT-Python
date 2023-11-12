s = input().split()
n,m = int(s[0]),int(s[1])
a = []
for i in range(n):
    b = [int(x) for x in input().split()]
    a.append(b)
if n > m:
    tmp = n
    i = 0
    while tmp > m:
        a.remove(a[i])
        i += 1
        tmp -= 1
    n = tmp
elif m > n:
    tmp = m
    i = 1
    while tmp > n:
        for j in range(n):
            a[j][i] = -1
        i += 2
        tmp -= 1
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            continue
        print(a[i][j],end = ' ')
    print()
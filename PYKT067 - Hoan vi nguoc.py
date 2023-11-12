a = ['0' for x in range(11)]
vis = [0 for x in range(11)]

def Try(i):
    if i > n:
        print(''.join(a[1:n + 1]),end= ' ')
        return
    for j in range(n,0,-1):
        if vis[j] == 0:
            vis[j] = 1
            a[i] = str(j)
            Try(i + 1)
            vis[j] = 0

t = int(input())
for i in range(t):
    n = int(input())
    fac = 1
    for j in range(1,n + 1):
        fac *= j
    print(fac)
    Try(1)
    print()
    
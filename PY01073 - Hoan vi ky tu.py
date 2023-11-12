s = input()
n = len(s)
a = ['0' for x in range(n)]
vis = [0 for x in range(n)]


def Try(i):
    if(i == n):
        res = [a[x] for x in range(0, n)]
        print("".join(res))
        return
    for j in range(n):
        if(vis[j] == 0):
            vis[j] = 1
            a[i] = s[j]
            Try(i + 1)
            vis[j] = 0

Try(0)
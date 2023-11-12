s = input().split()
n,m = int(s[0]),int(s[1])
b = []
luckymax = 0
luckymin = 10001
for i in range(n):
    a = [int(x) for x in input().split()]
    tmpmax = max(a)
    tmpmin = min(a)
    luckymin = min(tmpmin,luckymin)
    luckymax = max(luckymax,tmpmax)
    b.append(a)
luckynumber = luckymax - luckymin
c = 0
for i in range(n):
    for j in range(m):
        if b[i][j] == luckynumber:
            c = 1
            break
if c == 0:
    print("NOT FOUND")
else:
    print(luckynumber)
    for i in range(n):
        for j in range(m):
            if b[i][j] == luckynumber:
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
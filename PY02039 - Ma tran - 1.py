n = int(input())
b = []
for i in range(n):
    a = [int(x) for x in input().split()]
    b.append(a)
k = int(input())
s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif i < j:
            s += b[i][j]
        else:
            s -= b[i][j]
if abs(s) <= k:
    print("YES")
else:
    print("NO")
print(abs(s))
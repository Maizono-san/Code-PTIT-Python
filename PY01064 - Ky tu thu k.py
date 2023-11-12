t = int(input())
for i in range(t):
    a = input().split()
    n,k = int(a[0]), int(a[1])
    s = ''
    for j in range(n):
        s = s + chr(65 + j) + s
    print(s[k - 1])
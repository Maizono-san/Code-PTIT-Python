t = int(input())
for i in range(t):
    s = input().split()
    n,d = int(s[0]),int(s[1])
    a = [int(x) for x in input().split()]
    for j in range(d,n):
        print(a[j],end=' ')
    for j in range(0,d):
        print(a[j],end=' ')
    print()
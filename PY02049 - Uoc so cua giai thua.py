t = int(input())
for k in range(t):
    s = input().split()
    n,p = int(s[0]),int(s[1])
    count = 0
    for i in range(2,n + 1):
        tmp = i
        while tmp % p == 0:
            tmp //= p
            count += 1
    print(count)
        
s = input().split()
a,k,n = int(s[0]),int(s[1]),int(s[2])
b = k - a % k
if a + b > n:
    print(-1)
else:
    while(a + b <= n):
        print(b,end = ' ')
        b += k
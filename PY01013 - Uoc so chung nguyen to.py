from math import sqrt,gcd
t = int(input())
for i in range(t):
    s = input().split()
    a,b = int(s[0]),int(s[1])
    c = gcd(a,b)
    s = 0
    while c > 0:
        s += c % 10
        c //= 10
    if s < 2:
        print("NO")
    else:
        check = 0
        for j in range(2,int(sqrt(s))+1):
            if(s % j == 0):
                print("NO")
                check = 1
                break
        if(check == 0):
            print("YES")
    

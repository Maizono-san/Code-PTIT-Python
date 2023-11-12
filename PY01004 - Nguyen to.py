from math import gcd,sqrt
t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    for j in range(1,n):
        if gcd(j,n) == 1:
            count += 1
    if(count < 2):
        print("NO")
    else:
        c = 0
        for k in range(2,int(sqrt(count)) + 1):
            if(count%k == 0):
                print("NO")
                c = 1
                break
        if c == 0:
            print("YES")
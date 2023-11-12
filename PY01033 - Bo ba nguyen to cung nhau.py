from math import gcd

s = input().split()
l,r = int(s[0]),int(s[1])
for i in range(l,r-1):
    for j in range(i+1,r):
        for k in range(j+1,r+1):
            if gcd(i,j) != 1:
                break
            if gcd(j,k) != 1 or gcd(k,i) != 1:
                continue
            print("(" + str(i) + ",",str(j) + ",",str(k) + ")")
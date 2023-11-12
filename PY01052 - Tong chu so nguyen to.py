from math import sqrt

def sum(s):
    tong = 0
    for i in s:
        tong += int(i)
    return tong

def prime(a):
    if a < 2:
        return False
    else:
        for i in range(2,int(sqrt(a))+1):
            if(a % i == 0):
                return False
        return True

t = int(input())
for i in range(t):
    n = input()
    s = sum(n)
    if(prime(s)):
        print("YES")
    else:
        print("NO")
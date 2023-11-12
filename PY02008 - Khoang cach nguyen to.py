from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

s = input().split()
n,x = int(s[0]),int(s[1])
i = 0
j = 2
while i <= n:
    if prime(j):
        print(x,end = ' ')
        x += j
        i += 1
    j += 1
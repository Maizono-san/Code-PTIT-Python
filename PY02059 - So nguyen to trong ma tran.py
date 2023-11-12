from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

s = input().split()
n,m = int(s[0]),int(s[1])
b = []
primemax = 0
for i in range(n):
    a = [int(x) for x in input().split()]
    for j in range(len(a)):
        if not prime(a[j]):
            a[j] = 0
    tmp = max(a)
    primemax = max(tmp,primemax)
    b.append(a)
if primemax == 0:
    print("NOT FOUND")
else:
    print(primemax)
    for i in range(n):
        for j in range(m):
            if b[i][j] == primemax:
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
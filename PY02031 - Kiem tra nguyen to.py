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
for i in range(n):
    a = [int(x) for x in input().split()]
    b.append(a)
for i in range(n):
    for j in range(m):
        if prime(b[i][j]):
            b[i][j] = 1
        else:
            b[i][j] = 0
for i in range(n):
    for j in range(m):
        print(b[i][j],end = ' ')
    print()


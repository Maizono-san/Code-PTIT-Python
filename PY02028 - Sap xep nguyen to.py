from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n


n = int(input())
a = [int(x) for x in input().split()]
for i in range(n - 1):
    for j in range(i + 1,n):
        if prime(a[i]) and prime(a[j]):
            if a[i] > a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
for i in range(n):
    print(a[i],end=' ')
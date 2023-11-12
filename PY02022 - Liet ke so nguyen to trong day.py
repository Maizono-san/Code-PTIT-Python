from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
for i in range(len(a)):
    if prime(a[i]):
        print(a[i],a.count(a[i]))
        b = a[i]
        while a.count(b) > 0:
            a.remove(b)
            a.insert(0,0)
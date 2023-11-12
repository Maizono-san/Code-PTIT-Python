from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n))):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if i > 0:
        b.append(i)
        while a.count(i) > 0:
            a.remove(i)
            a.insert(0,0)
s1 = 0
s2 = sum(b)
c = 0
for i in range(len(b)):
    s1 += b[i]
    s2 -= b[i]
    if prime(s1) and prime(s2):
        print(i)
        c = 1
        break
if c == 0:
    print("NOT FOUND")
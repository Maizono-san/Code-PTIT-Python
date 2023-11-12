from math import sqrt
from collections import Counter

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n))):
        if n % i == 0:
            return False
    return True

n = int(input())
a = Counter([int(x) for x in input().split()])
s1 = 0
s2 = sum(a)
c = 0
count = 0
for i in a:
    s1 += i
    s2 -= i
    if prime(s1) and prime(s2):
        print(count)
        c = 1
        break
    count += 1
if c == 0:
    print("NOT FOUND")
from math import sqrt

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True        

t = int(input())
for i in range(t):
    s = input()
    s1,s2 = s[:3],s[-3:]
    if prime(int(s1)) and prime(int(s2)):
        print("YES")
    else:
        print("NO")
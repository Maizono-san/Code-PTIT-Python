from math import sqrt

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

t = int(input())
for i in range(t):
    s = input()
    c = 0
    for j in range(len(s)):
        if prime(j):
            if not prime(int(s[j])):
                print("NO")
                c = 1
                break
        else:
            if prime(int(s[j])):
                print("NO")
                c = 1
                break
    if c == 0:
        print("YES")
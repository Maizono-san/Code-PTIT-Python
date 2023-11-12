from math import sqrt

def sum(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong

def prime(n):
    if n < 2:
        return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    s1 = s[::-1]
    c = 0
    for j in range(len(s)):
        if not prime(int(s[j])):
            c = 1
            print("No")
            break
    if c == 0:
        if prime(int(s)) and prime(int(s1)) and prime(sum(s)):
            print("Yes")
        else:
            print("No")
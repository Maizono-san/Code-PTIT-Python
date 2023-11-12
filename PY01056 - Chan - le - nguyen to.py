from math import sqrt

def sum(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong

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
        if j % 2 == 0 and int(s[j]) % 2 == 0:
            continue
        elif j % 2 == 1 and int(s[j]) % 2 == 1:
            continue
        c = 1
        break
    if c == 0 and prime(sum(s)):
        print("YES")
    else:
        print("NO")
from math import gcd
t = int(input())
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    if gcd(int(s1), int(s2)) == 1:
        print("YES")
    else:
        print("NO")



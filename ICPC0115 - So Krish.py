def fac(n):
    mul = 1
    for i in range(1,n + 1):
        mul *= i
    return mul

t = int(input())
for i in range(t):
    s = input()
    sum = 0
    for j in range(len(s)):
        sum += fac(int(s[j]))
    if sum == int(s):
        print("Yes")
    else:
        print("No")


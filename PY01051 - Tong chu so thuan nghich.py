def sum(s):
    tong = 0
    for i in s:
        tong += int(i)
    return tong

def reverse(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

t = int(input())
for i in range(t):
    n = input()
    s = sum(n)
    if len(str(s)) < 2:
        print("NO")
    else:
        if reverse(str(s)):
            print("YES")
        else:
            print("NO")

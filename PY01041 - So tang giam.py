def check(s):
    if len(s) < 3:
        return False
    b = -1
    for i in range(len(s) - 2):
        if s[i] >= s[i + 1]:
            b = i
            break
    if b == 0:
        return False
    else:
        for j in range(b,len(s) - 1):
            if s[j] <= s[j + 1]:
                return False
        return True

t = int(input())
for i in range(t):
    s = input()
    s += '.'
    if check(s):
        print("YES")
    else:
        print("NO")

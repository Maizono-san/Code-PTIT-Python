t = int(input())
for i in range(t):
    s = input()
    c = 0
    for j in range(len(s)):
        if s[j] != '0' and s[j] != '1' and s[j] != '2':
            print("NO")
            c = 1
            break
    if c == 0:
        print("YES")
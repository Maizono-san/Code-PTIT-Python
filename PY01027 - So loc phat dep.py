s = input()
n = len(s)
s += '   '
c = 0
if s[0] != '6':
    print("NO")
else:
    for i in range(1,n):
        if s[i] != '6' and s[i] != '8':
            print("NO")
            c = 1
            break
        elif s[i] == '8' and s[i + 1] == '8' and s[i + 2] == '8':
            print("NO")
            c = 1
            break
    if c == 0:
        print("YES")
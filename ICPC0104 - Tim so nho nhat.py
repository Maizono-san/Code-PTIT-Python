t = int(input())
for i in range(t):
    s = input()
    s += '.'
    s1 = ''
    a = []
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            s1 += s[j]
        else:
            if s1 != '':
                a.append(int(s1))
                s1 = ''
    a.sort()
    print(a[0])
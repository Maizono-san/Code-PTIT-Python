t = int(input())
a = []
for i in range(t):
    s = input()
    s += '.'
    tmp = ''
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            tmp += s[j]
            if s[j + 1] < '0' or s[j + 1] > '9':
                a.append(int(tmp))
                tmp = ''
a.sort()
for i in a:
    print(i)
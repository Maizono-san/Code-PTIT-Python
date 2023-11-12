t = int(input())
s = ''
for i in range(t):
    s += str(len(input().split()))
s += '.'
s = s.replace('7777', '1')
a = []
for i in range(len(s)-1):
    if s[i] == '8':
        if s[i+1] != '6':
            a.append(1)
    if s[i] == '1':
        a.append(2)
print(len(a))
for x in a:
    print(x)
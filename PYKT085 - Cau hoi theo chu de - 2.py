t = int(input())
a = []
b = []
count = 0
for i in range(t):
    s = input()
    if s != '' and i < t - 1:
        b.append(s)
    elif s == '':
        a.append(b)
        b = []
    elif i == t - 1:
        b.append(s)
        a.append(b)
for i in range(len(a)):
    print(a[i][0] + ': ' + str(len(a[i]) - 1))
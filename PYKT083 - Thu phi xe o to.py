t = int(input())
a = []
b = set()
for i in range(t):
    s = input()
    tmp = s[11:].split()
    tmp.remove(tmp[0])
    a.append(tmp)
    b.add(tmp[2])
b = sorted(list(b))
count = [0 for x in range(len(b))]
for i in range(t):
    if a[i][1] == 'OUT':
        continue
    else:
        for j in range(len(b)):
            if a[i][2] == b[j]:
                if a[i][0] == '5':
                    count[j] += 10000
                elif a[i][0] == '7':
                    count[j] += 15000
                elif a[i][0] =='2':
                    count[j] += 20000
                elif a[i][0] == '29':
                    count[j] += 50000
                elif a[i][0] == '45':
                    count[j] += 70000
for i in range(len(b)):
    print(b[i] + ': ' + str(count[i]))
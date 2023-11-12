def fac(n):
    s = 1
    for i in range(2,n + 1):
        s *= i
    return s
n = int(input())
a = []
for i in range(n):
    b = [x for x in input()]
    a.append(b)
count = 0
for i in range(n):
    countcoin = 0
    for j in range(n):
        if a[i][j] == 'C':
            countcoin += 1
    if countcoin < 2:
        continue
    count += int(fac(countcoin)/(fac(2)*fac(countcoin - 2)))
for i in range(n):
    countcoin = 0
    for j in range(n):
        if a[j][i] == 'C':
            countcoin += 1
    if countcoin < 2:
        continue
    count += int(fac(countcoin)/(fac(2)*fac(countcoin - 2)))
print(count)

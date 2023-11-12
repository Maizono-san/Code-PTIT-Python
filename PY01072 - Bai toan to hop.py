s = input().split()
n,k = int(s[0]),int(s[1])
a = sorted(list(set(int(x) for x in input().split())))
b = [x for x in range(1,k + 1)]
while True:
    for i in range(k):
        print(a[b[i] - 1],end = " ")
    print()
    i = k - 1
    while(i >= 0 and b[i] >= len(a) - k + i + 1):
        i -= 1
    if i < 0:
        break
    b[i] += 1
    for j in range(i + 1,k):
        b[j] = b[i] + j - i
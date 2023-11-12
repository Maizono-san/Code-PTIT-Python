n = int(input())
a = []
while len(a) < n:
    a.extend(int(x) for x in input().split())
for i in range(n - 1):
    for j in range(i + 1,n):
        if a[i] % 2 == 0 and a[j] % 2 == 0:
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
        elif a[i] % 2 == 1 and a[j] % 2 == 1:
            if a[i] < a[j]:
                a[i],a[j] = a[j],a[i]
for i in a:
    print(i,end = ' ')
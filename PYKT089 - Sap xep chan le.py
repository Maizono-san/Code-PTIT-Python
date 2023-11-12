n = int(input())
a = []
while len(a) < n:
    a.extend(int(x) for x in input().split())
for i in range(len(a) - 1):
    for j in range(i + 1,len(a)):
        if a[i] % 2 == 0 and a[j] % 2 == 0:
            if a[i] > a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
        elif a[i] % 2 == 1 and a[j] % 2 == 1:
            if a[i] < a[j]:
                x = a[i]
                a[i] = a[j]
                a[j] = x
    print(a[i],end = ' ')
print(a[len(a) - 1])
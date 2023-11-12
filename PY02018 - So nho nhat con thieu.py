n = int(input())
a = [int(x) for x in input().split()]
a.sort()
c = 0
for i in range(len(a)-1):
    if int(a[i + 1]) != int(a[i]) + 1:
        print(int(a[i]) + 1)
        c = 1
        break
if c == 0:
    print(int(a[n - 1]) +1)
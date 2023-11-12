n = int(input())
a = []
while len(a) < n:
    a.extend(int(x) for x in input().split())
maxarray = max(a)
j = 0
c = 0
for i in range(1, maxarray):
    if i != a[j]:
        print(i)
        c = 1
    else:
        j += 1
if c == 0:
    print("Excellent!")

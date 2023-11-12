n = int(input())
a = [int(x) for x in input().split()]
while True:
    c = 0
    j = 0
    while j < len(a) - 1:
        if (int(a[j]) + int(a[j + 1])) % 2 == 0:
            a.pop(j)
            a.pop(j)
            c = 1
        else:
            j += 1
    if c == 0:
        break
print(len(a))
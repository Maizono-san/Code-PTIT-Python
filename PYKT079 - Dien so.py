t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    count = 0
    for j in range(min(a) + 1,max(a)):
        if a.count(j) == 0:
            count += 1
    print(count)

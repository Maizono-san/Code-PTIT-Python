def process(s):
    sum = 0
    s1 = str(s)
    for i in range(len(s1)):
        sum += int(s1[i])
    return sum

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a.sort(key=process)
    for j in a:
        print(j,end=' ')
    print()

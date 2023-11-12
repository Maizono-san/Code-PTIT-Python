def process(s):
    mul = 1
    s1 = str(s)
    for i in range(len(s1)):
        mul *= int(s1[i])
    return mul

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    a.sort(key=process)
    for j in a:
        print(j,end=' ')
    print()
from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        a.append(int(input()))
    dic = Counter(sorted(a))
    m = max(dic,key = lambda x: dic[x])
    print(m)


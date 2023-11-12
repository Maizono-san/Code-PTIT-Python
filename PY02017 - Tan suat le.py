from collections import Counter

t = int(input())
for i in range(t):
    n = int(input())
    dic = Counter([int(x) for x in input().split()])
    for j in dic:
        if dic[j] % 2 == 1:
            print(j)
            break
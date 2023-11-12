from collections import Counter

def process():
    n = int(input())
    dic = Counter(sorted([int(x) for x in input().split()]))
    m = max(dic, key = lambda x: dic[x])
    print(m) if dic[m] > n//2 else print('NO')

t = int(input())
for i in range(t):
    process()
from collections import Counter

s = input().split()
n,m = int(s[0]),int(s[1])
dic = Counter(sorted(([int(x) for x in input().split()])))
m1 = max(dic,key = lambda x : dic[x])
m2,key2 = 0,0
for i in dic:
    if dic[i] > key2 and dic[m1] > dic[i]:
        key2= dic[i]
        m2 = i
if m2 == 0:
    print('NONE')
else:
    print(m2)
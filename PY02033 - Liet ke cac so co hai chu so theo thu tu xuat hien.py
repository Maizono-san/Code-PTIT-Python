from collections import Counter

s = input()
a = []
for i in range(0,len(s) - 1,2):
    a.append(s[i:i+2])
b = Counter(a)
for i in b:
    print(i,end=' ')
    
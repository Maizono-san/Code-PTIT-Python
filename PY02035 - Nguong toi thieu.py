from collections import Counter

s = input()
k = int(input())
a = []
for i in range(0,len(s) - 1,2):
    a.append(s[i:i + 2])
b = Counter(sorted(a))
c = 0
for i in b:
    if b[i] >= k:
        print(i,b[i])
        c = 1
if c == 0:
    print("NOT FOUND")
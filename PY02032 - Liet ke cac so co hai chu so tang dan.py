s = input()
a = set()
for i in range(0,len(s) - 1,2):
    a.add(s[i:i+2])
b = sorted(a)
for i in b:
    print(i,end=' ')
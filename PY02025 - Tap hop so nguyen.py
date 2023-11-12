s = input().split()
n,m = int(s[0]),int(s[1])
a = set(int(x) for x in input().split())
b = set(int(y) for y in input().split())
c = sorted(a.intersection(b))
d = sorted(a.difference(b))
e = sorted(b.difference(a))
for i in c:
    print(i,end=' ')
print()
for i in d:
    print(i,end=' ')
print()
for i in e:
    print(i,end=' ')
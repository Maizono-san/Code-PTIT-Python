n = int(input())
a = [float(x) for x in input().split()]
b = min(a)
c = max(a)
while a.count(b) > 0:
    a.remove(b)
while a.count(c) > 0:
    a.remove(c)
s = 0
for i in a:
    s += i
print("{:.2f}".format(s/len(a)))

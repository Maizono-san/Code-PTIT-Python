s = input().split()
n,m = int(s[0]),int(s[1])
a = set(int(x) for x in input().split())
b = set(int(y) for y in input().split())
if a == b:
    print("YES")
else:
    print("NO")
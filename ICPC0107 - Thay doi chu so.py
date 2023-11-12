def minsum(x1,x2,p,q):
    if int(p) < int(q):
        x1 = x1.replace(q,p)
        x2 = x2.replace(q,p)
    elif int(p) > int(q):
        x1 = x1.replace(p,q)
        x2 = x2.replace(p,q)
    return int(x1) + int(x2)

def maxsum(x1,x2,p,q):    
    if int(p) < int(q):
        x1 = x1.replace(p,q)
        x2 = x2.replace(p,q)
    elif int(p) > int(q):
        x1 = x1.replace(q,p)
        x2 = x2.replace(q,p)
    return int(x1) + int(x2)




t = int(input())
for i in range(t):
    s = input().split()
    p,q = s[0],s[1]
    a = []
    while len(a) < 2:
        a.extend(input().split())
    x1,x2 = a[0],a[1]
    print(minsum(x1,x2,p,q),maxsum(x1,x2,p,q))
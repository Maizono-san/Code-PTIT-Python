def change(n,b):
    s = ''
    while n > 0:
        s += str(n % b) + ' '
        n //= b
    for i in range(10,36):
        s = s.replace(str(i),chr(i + 55))
    s = s.replace(' ','')
    return s[::-1]

t = int(input())
for i in range(t):
    a = input().split()
    n,b = int(a[0]),int(a[1])
    print(change(n,b))
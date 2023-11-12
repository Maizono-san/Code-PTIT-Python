t = int(input())
for i in range(0,t):
    a = input()
    l = len(a)
    if a[0] == a[l - 2] and a[1] == a[l - 1]:
        print("YES")
    else:
        print("NO")
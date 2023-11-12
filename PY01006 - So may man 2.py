t = int(input())
for i in range(0,t):
    a = input()
    b = 0
    for j in a:
        if j != '4' and j != '7':
            print("NO")
            b = 1
            break
    if b == 0:
        print("YES")
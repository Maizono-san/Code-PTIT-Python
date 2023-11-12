t = int(input())
for i in range(t):
    s = input().split('.')
    c = 0
    if len(s) != 4:
        print("NO")
    else:
        for j in s:
            if j < '0' or j > '255':
                print("NO")
                c = 1
                break
        if c == 0:
            print("YES")
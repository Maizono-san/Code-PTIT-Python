t = int(input())
for i in range(t):
    s = input()
    b = 0
    for i in range(0,len(s) - 1):
        if(s[i] > s[i + 1]):
            print("NO")
            b = 1
            break
    if b == 0:
        print("YES")
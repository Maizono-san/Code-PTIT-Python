t = int(input())
for i in range(t):
    a = input()
    s = 0
    b = 0
    for j in range(len(a) - 1):
        if int(a[j]) - int(a[j+1]) != 2 and int(a[j+1]) - int(a[j]) != 2:
            b = 1
            print("NO")
            break
    if b == 0:
        for k in range(len(a)):
            s += int(a[k])
        if s % 10 == 0:
            print("YES")
        else:
            print("NO")
    

    



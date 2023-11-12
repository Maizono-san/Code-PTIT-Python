from math import sqrt
t = int(input())
for i in range(t):
    n = input()  
    s = n[-4:]  
    c = 0
    if int(s) < 2:
       print("NO")
    else:
        for j in range(2,int(sqrt(int(s))) + 1):
            if int(s) % j == 0:
                print("NO")
                c = 1
                break
        if c == 0:
            print("YES")
from math import sqrt
t = int(input())
for i in range(t):
    n = int(input())
    print(1,end =' ')
    for j in range(2,int(sqrt(n)) + 1):
        if(n % j == 0):
            pow = 0
            while(n % j == 0):
                pow += 1
                n //= j
            print("*",str(j)+"^"+str(pow),end=' ')
    if(n > 1):
        print("*",str(n)+"^1")
    else:
        print()

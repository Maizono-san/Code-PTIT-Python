from math import gcd
s = input().split(' ')
a,b = int(s[0]),int(s[1])
count = 0
for i in range(10**(b-1),10**b-1):
    if(gcd(a,i) == 1):
        print(i,end=' ')
        count += 1
        if(count == 10):
            print()
            count = 0

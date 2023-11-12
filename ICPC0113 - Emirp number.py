from math import sqrt
N = 1_000_001
prime = [True for x in range(N)]
prime[0] = prime[1] = False
for i in range(2,int(sqrt(N) + 1)):
    if not prime[i]:
        continue
    for j in range(i*i,N,i):
        prime[j] = False

t = int(input())
for i in range(t):
    s = int(input())
    for j in range(1,s):
        if prime[j]:
            a = int(str(j)[::-1])
            if a > j and prime[a] and a < int(s):
                print(j,a,end=' ')
    print()

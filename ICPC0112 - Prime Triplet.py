from math import *
N = 1_000_001
prime = [True for x in range(N)]
prime[0] = prime[1] = False
for i in range(2,int(sqrt(N) + 1)):
    if not prime[i]:
        continue
    else:
        for j in range(i * i,N,i):
            prime[j] = False

t = int(input())
for t1 in range(t):
    count = 0
    n = int(input())
    for i in range(2,n - 6):
        if (prime[i] and prime[i + 2] and  prime[i + 6]) or (prime[i] and prime[i + 4] and  prime[i + 6]):
            count += 1
    print(count)
INF = 100_001
prime = [True for x in range(INF)]
a = []

prime[0],prime[1] = False,False
for i in range(2,INF):
    if not prime[i]:
        continue
    else:
        a.append(i)
        for j in range(i + i,INF,i):
            prime[j] = False

n = int(input())
count = 0
for i in range(len(a)):
    if a[i]**8 > n:
        break
    else:
        count += 1
for i in range(len(a) - 1):
    if a[i]**2 <= n:
        for j in range(i + 1,len(a)):
            if a[i]**2 * a[j]**2 > n:
                break
            else:
                count += 1
print(count)
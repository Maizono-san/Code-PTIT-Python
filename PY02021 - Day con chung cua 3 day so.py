def intersection():
    arr = input().split()
    n, m, k = int(arr[0]), int(arr[1]), int(arr[2])
    s1 = [int(x) for x in input().split()]
    s2 = [int(x) for x in input().split()]
    s3 = [int(x) for x in input().split()]
    p, q = [], []
    i = j = 0
    while i < n and j < m:
        if s1[i] < s2[j]:
            i += 1
        elif s1[i] > s2[j]: 
            j += 1
        else:
            p.append(s1[i])
            i += 1
            j += 1
    
    i = j = 0
    if(len(p) == 0):
        print("NO")
        return
    while i < k and j < len(p):
        if s3[i] < p[j]:
            i += 1
        elif s3[i] > p[j]: 
            j += 1
        else:
            q.append(s3[i])
            i += 1
            j += 1
    
    if(len(q) == 0):
        print("NO")
    else:
        for x in q:
            print(x, end=" ")
        print()
    
t = int(input())
for i in range(t):
    intersection()
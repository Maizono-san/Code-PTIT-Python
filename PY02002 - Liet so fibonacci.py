t = int(input())
for i in range(t):
    s = input().split()
    a,b = int(s[0]),int(s[1])
    arr = [1 , 1]
    for j in range(2,b):
        arr.append(arr[j - 1] + arr[j - 2])
    for k in range(a - 1,b):
        print(arr[k],end=' ')
    print()
    
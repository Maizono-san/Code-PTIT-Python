def reverse(s):
    if len(s) < 2:
        return False
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

s = input().split()
n,m = int(s[0]),int(s[1])
b = []
reversemax = 0
for i in range(n):
    a = [int(x) for x in input().split()]
    for j in range(len(a)):
        if not reverse(str(a[j])):
            a[j] = 0
    tmp = max(a)
    reversemax = max(tmp,reversemax)
    b.append(a)
if reversemax == 0:
    print("NOT FOUND")
else:
    print(reversemax)
    for i in range(n):
        for j in range(m):
            if b[i][j] == reversemax:
                print("Vi tri [" + str(i) + "][" + str(j) + "]")
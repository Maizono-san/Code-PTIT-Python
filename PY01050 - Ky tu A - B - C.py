a = [0 for x in range(13)]
count = [0 for x in range(3)]

def Try(i):
    if i > n:
        if count[0] == 0 or count[1] == 0 or count[2] == 0:
            return
        if count[0] > count[1]:
            return
        if count[1] > count[2]:
            return
        print(''.join(a[1:n + 1]))
        return
    for j in range(65, 68):
        a[i] = chr(j)
        count[j - 65] += 1
        Try(i+1)
        count[j - 65] -= 1
t = int(input())
for i in range(3, t + 1):
    n = i
    Try(1)
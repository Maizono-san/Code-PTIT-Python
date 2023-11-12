arr = [0 for x in range(10)]

def Try(i):
    if i > m:
        s = ''
        for j in range(1, m+1):
            s += str(arr[j])
        s = s + s[::-1]
        if int(s) >= n:
            global ok
            ok = True
            return
        print(s, end=' ')
        return

    for j in range(0, 9, 2):
        if ok:
            return
        if i == 1 and j == 0:
            continue
        arr[i] = j
        Try(i+1)

def main():
    global n, m, ok
    ok = False
    n = int(input())
    m = 1
    while not ok:
        Try(1)
        m += 1
    print()

t = int(input())
for i in range(t):
    main()
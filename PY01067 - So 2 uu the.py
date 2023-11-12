arr = [0 for x in range(20)]

def Try(i):
    if i > tmp:
        if arr[1:i].count('2') > tmp//2:
            global ok, cnt
            print("".join(arr[1:i]), end = ' ')
            cnt += 1
            if cnt == n:
                ok = True
        return

    for j in range(3):
        if ok:
            return
        if i == 1 and j == 0:
            continue
        arr[i] = str(j)
        Try(i+1)

test = int(input())
for i in range(test):
    n, tmp , cnt, ok = int(input()), 1, 0, False
    while not ok:
        Try(1)
        tmp += 1
    print()
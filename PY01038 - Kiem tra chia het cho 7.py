t = int(input())
for i in range(t):
    n = int(input())
    count = 0
    while True:
        if count == 1000:
            break
        elif n % 7 == 0:
            print(n)
            break
        else:
            count += 1
            a = str(n)
            rev = a[::-1]
            n += int(rev)

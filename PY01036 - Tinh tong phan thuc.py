t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    chan = 2
    le = 1
    if n % 2 == 0:
        while chan <= n:
            s += 1/chan
            chan += 2
    else:
        while le <= n:
            s += 1/le
            le += 2
    print("{:.6f}".format(s))

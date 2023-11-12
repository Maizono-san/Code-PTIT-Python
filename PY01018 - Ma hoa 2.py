while True:
    a = input().split(' ')
    try:
        k,s = int(a[0]),str(a[1])
    except IndexError:
        break
    else:
        p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
        lst = []
        j = 0
        while j < len(s):
            for i in range(len(p)):
                if s[j] == p[i]:
                    lst.append(p[(i+k)%28])
                    j += 1
                    break
        lst.reverse()
        print("".join(lst))

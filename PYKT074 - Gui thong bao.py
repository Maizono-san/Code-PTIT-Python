t = int(input())
for i in range(t):
    s = input()
    tmp = ""
    if len(s) <= 100:
        print(s)
    else:
        a = s.split()
        for j in range(len(a)):
            res = tmp
            tmp += a[j]
            if len(tmp) > 100:
                tmp = res
                break
            tmp += " "
        print(tmp)
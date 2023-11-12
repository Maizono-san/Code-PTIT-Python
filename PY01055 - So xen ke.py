t = int(input())
for i in range(t):
    s = input()
    c = 0
    if len(s) % 2 != 0 and s[0] != s[1]:
        j = 0
        while j < len(s) - 2:
            if s[j] != s[j + 2]:
                print("NO")
                c = 1
                break
            j += 2
        if c == 0:
            print("YES")
    else:
        print("NO")

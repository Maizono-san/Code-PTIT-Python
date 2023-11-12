t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    s += '.'
    count = 1
    for j in range(n):
        if(s[j] == s[j+1]):
            count += 1
        else:
            print(str(count)+s[j],end="")
            count = 1
    print()

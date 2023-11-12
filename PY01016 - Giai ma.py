from re import A


t = int(input())
for i in range(t):
    s = input()
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            a = int(s[j])
            while a >= 1:
                print(s[j - 1],end='')
                a -= 1
    print()
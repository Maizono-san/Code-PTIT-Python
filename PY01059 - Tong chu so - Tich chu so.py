t = int(input())
for i in range(t):
    sum,mul = 0,1
    s = input()
    c = 0
    for j in range(len(s)):
        if j % 2 == 0:
            sum += int(s[j])
        else:
            if int(s[j]) == 0:
                continue
            mul *= int(s[j])
            c = 1
    if c == 0:
        mul = 0
    print(sum,mul)

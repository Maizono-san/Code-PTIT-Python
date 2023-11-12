t = int(input())
for i in range(t):
    s = input()
    mul = 1
    for j in range(len(s)):
        if s[j] == '0':
            continue
        mul = mul * int(s[j])
    print(mul)
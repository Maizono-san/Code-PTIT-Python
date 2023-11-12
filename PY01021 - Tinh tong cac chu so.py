t = int(input())
for i in range(t):
    s = list(input())
    s.sort()
    sum = 0
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            sum += int(s[j])
    for j in range(len(s)):
        if s[j] >= '0' and s[j] <= '9':
            continue
        print(s[j],end='')
    print(sum)
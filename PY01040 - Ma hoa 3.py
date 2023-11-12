t = int(input())
for i in range(t):
    s = input()
    n = len(s)//2
    s1 = list(s[:n])
    s2 = list(s[n:])
    sum1,sum2 = 0,0
    for j in range(n):
        sum1 += ord(s1[j]) - 65
        sum2 += ord(s2[j]) - 65
    for j in range(n):
        k1 = (ord(s1[j]) - 65 + sum1) % 26
        k2 = (ord(s2[j]) - 65 + sum2) % 26
        s1[j] = chr(k1 + 65)
        s2[j] = chr(k2 + 65)
        k3 = (ord(s1[j]) - 65 + ord(s2[j]) - 65) % 26
        s1[j] = chr(k3 + 65)
    print(''.join(s1))
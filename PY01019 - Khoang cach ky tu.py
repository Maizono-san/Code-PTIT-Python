t = int(input())
for i in range(t):
    s1 = input()
    s2 = s1[::-1]
    a = 0
    for j in range(1,len(s1)):
        if abs(ord(s1[j]) - ord(s1[j-1])) != abs(ord(s2[j]) - ord(s2[j-1])):
            print("NO")
            a = 1
            break
    if a == 0:
        print("YES")

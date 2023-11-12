a = input()
b = 0
c = 0
for i in a:
    if i == '4':
        b += 1
    if i == '7':
        c += 1
if b + c == 4 or b + c == 7:
    print("YES")
else:
    print("NO")
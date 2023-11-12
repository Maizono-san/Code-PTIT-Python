a = input()
hoa = 0
thuong = 0
for i in a:
    if i >= 'a' and i <= 'z':
        thuong += 1
    if i >= 'A' and i <= 'Z':
        hoa += 1
if thuong >= hoa:
    b = a.lower()
    print(b)
else:
    c = a.upper()
    print(c)
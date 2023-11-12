t = int(input())
for i in range(t):
    b = int(input())
    n = int(input(),2)
    if b == 2:
        s2 = bin(n)
        print(s2[2:])
    elif b == 4:
        s4 = ''
        while n > 0:
            s4 += str(n % 4)
            n //= 4
        print(s4[::-1])
    elif b == 8:
        s8 = oct(n)
        print(s8[2:])
    elif b == 16:
        s16 = hex(n)
        print(s16[2:].upper())
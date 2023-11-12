def change(n):
    if n == 3 or n == 4:
        return 2.5
    elif n == 5 or n == 6:
        return 3.0
    elif n >= 7 and n <= 9:
        return 3.5
    elif n >= 10 and n <= 12:
        return 4.0
    elif n >= 13 and n <= 15:
        return 4.5
    elif n >= 16 and n <= 19:
        return 5.0
    elif n >= 20 and n <= 22:
        return 5.5
    elif n >= 23 and n <= 26:
        return 6.0
    elif n >= 27 and n <= 29:
        return 6.5
    elif n >= 30 and n <= 32:
        return 7.0
    elif n == 33 or n ==34:
        return 7.5
    elif n == 35 or n == 36:
        return 8.0
    elif n == 37 or n == 38:
        return 8.5
    elif n == 39 or n == 40:
        return 9.0


t = int(input())
for i in range(t):
    s = input().split()
    r,l,speaking,writing = int(s[0]),int(s[1]),float(s[2]),float(s[3])
    reading = change(r)
    listening = change(l)
    average = (reading + listening + speaking + writing)/4
    if(average >= int(average) + 0.25 and average < int(average) + 0.75):
        average = int(average) + 0.5
    elif(average < int(average) + 0.25):
        average = int(average) + 0.0
    elif(average >= int(average) + 0.75):
        average = int(average) + 1.0
    print(average)
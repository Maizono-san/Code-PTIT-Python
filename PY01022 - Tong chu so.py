def check(s):
    if int(s) < 0:
        if len(s) != 2:
            return False
        return True
    else:
        if len(s) != 1:
            return False
        return True
            

s = input()
sum,count = 0,0
while not check(s):
    if int(s) >= 0:
        for i in range(len(s)):
            sum += int(s[i])
        count += 1
        s = str(sum)
        sum = 0
    else:
        sum = -3
        for i in range(1, len(s)):
            sum += int(s[i])
        count += 1
        s = str(sum)
        sum = 0
print(count) 
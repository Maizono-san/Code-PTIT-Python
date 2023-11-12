t = int(input())
for i in range(t):
    s = input()
    lst = list(s[::-1])
    if len(lst) == 1:
        print(lst[0])
    else:
        for j in range(len(lst) - 1):
            if lst[j] < '5':
                lst[j] = '0'
            else:
                lst[j] = '0'
                lst[j+1] = str(int(lst[j+1]) + 1)
        lst.reverse()
        print("".join(lst))
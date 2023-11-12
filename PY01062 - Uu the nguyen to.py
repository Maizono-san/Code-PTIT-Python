from math import sqrt

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

t = int(input())
for i in range(t):
    s = input()
    count_prime,count_not_prime = 0,0
    for j in s:
        if prime(int(j)):
            count_prime += 1
        else:
            count_not_prime += 1
    if prime(count_prime + count_not_prime) and count_prime > count_not_prime:
        print("YES")
    else:
        print("NO")
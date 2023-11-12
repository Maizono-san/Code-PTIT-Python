def HanoiTower(n,a,b,c):
    if n == 1:
        print(a, "->",c)
        return
    HanoiTower(n - 1,a,c,b)
    print(a, "->",c)
    HanoiTower(n - 1,b,a,c)

n = int(input())
HanoiTower(n,'A','B','C')
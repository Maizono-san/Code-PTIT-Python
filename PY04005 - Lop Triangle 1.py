from math import *

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distance(self,z):
        a = self.x - z.x
        b = self.y - z.y
        d = sqrt(a * a + b * b)
        return d

class Triangle:
    def __init__(self,p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def output(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        if a + b <= c or b + c <= a or c + a <= b:
            print("INVALID")
        else:
            ans = a + b + c
            print('{:.3f}'.format(ans))

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triagle.output()
    i += 6
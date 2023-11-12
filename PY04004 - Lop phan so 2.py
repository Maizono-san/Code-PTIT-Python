from math import gcd

class Fraction:
    def __init__(self,tu,mau):
        self.tu = tu
        self.mau = mau
    def add(self,x):
        a = self.mau*x.tu + self.tu*x.mau
        b = self.mau*x.mau
        return Fraction(a,b)
    def process(self):
        c = gcd(self.tu,self.mau)
        self.tu = int(self.tu/c)
        self.mau = int(self.mau/c)
    def output(self):
        print(f'{self.tu}/{self.mau}')

p = [int(x) for x in input().split()]
a = Fraction(p[0],p[1])
b = Fraction(p[2],p[3])
c = a.add(b)
c.process()
c.output()
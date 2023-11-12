class Rectangle:
    def __init__(self,d,r,color):
        self.d = d
        self.r = r
        self.color = color.title()
    def check(self):
        if self.d <= 0 or self.r <= 0:
            return False
        return True
    def output(self):
        if self.check(): print((self.d + self.r)*2,self.d*self.r,self.color)
        else: print("INVALID")

s = input().split()
d,r,color = int(s[0]),int(s[1]),s[2]
rectangle = Rectangle(d,r,color)
rectangle.output()
    
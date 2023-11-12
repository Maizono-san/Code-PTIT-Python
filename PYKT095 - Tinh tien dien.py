class TienDien:
    tien1 = 0
    tien2 = 0
    vat = 0
    tong = 0
    def __init__(self,x, ma, ten,dau,cuoi):
        self.x = x
        self.ma = ma
        self.ten = ten
        s = cuoi - dau
        if x == 'A':
            if s < 100:
                self.tien1 = s*450
                self.tien2 = 0
                self.vat = 0
                self.tong = s*450
            else:
                self.tien1 = 100*450
                self.tien2 = (s - 100)*1000
                self.vat = (s - 100)*1000//20
                self.tong = 100*450 + (s - 100)*1000 + (s - 100)*1000//20
        elif x == 'B':
            if s < 500:
                self.tien1 = s*450
                self.tien2 = 0
                self.vat = 0
                self.tong = s*450
            else:
                self.tien1 = 500*450
                self.tien2 = (s - 500)*1000
                self.vat = (s - 500)*1000//20
                self.tong = 500*450 + (s - 500)*1000 + (s - 500)*1000//20
        elif x == 'C':
            if s < 200:
                self.tien1 = s*450
                self.tien2 = 0
                self.vat = 0
                self.tong = s*450
            else:
                self.tien1 = 200*450
                self.tien2 = (s - 200)*1000
                self.vat = (s - 200)*1000//20
                self.tong = 200*450 + (s - 200)*1000 + (s - 200)*1000//20
    def output(self) :
        print(self.ma, self.ten, self.tien1,self.tien2,self.vat,self.tong)



t = int(input())
a = []
for i in range(t):
    ten = input()
    ten = " ".join(ten.split())
    ten = ten.title()
    ma = "KH{:02d}".format(i + 1)
    s = input().split()
    x = s[0]
    dau,cuoi = int(s[1]),int(s[2])
    a.append(TienDien(x,ma,ten,dau,cuoi))

a = sorted(a, key= lambda x : (-x.tong))
for i in a :
    i.output()
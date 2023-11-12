class Gamer:
    timestr = ''
    timeint = 0
    def __init__(self, code, name, vao, ra):
        self.code = code
        self.name = name
        self.vao = vao
        self.ra = ra
        phut = round((float(ra[:2]) + float(ra[3:])/60 - (float(vao[:2]) + float(vao[3:])/60))*60)
        self.timeint = phut
        gio = 0
        while phut >= 60:
            phut -= 60
            gio += 1
        self.timestr = f'{gio} gio {phut} phut' 
    def output(self) :
        print(self.code, self.name, self.timestr)

a= []
for i in range(int(input())):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    a.append(Gamer(ma,ten,vao,ra))

a = sorted(a, key=lambda x : (-x.timeint))
for i in a:
    i.output()
class Average_grade:
    s = 0
    def __init__(self,id,name,s1,s2,s3):
        self.id = id
        self.name = name
        self.s = (s1*3 + s2*3 + s3*2)/8
    def output(self):
        print(self.id,self.name,"{:.2f}".format(self.s + 0.000001),end = ' ')

t = int(input())
a = []
for i in range(t):
    if i < 9:
        id = f'SV0{i+1}'
    else:
        id = f'SV{i+1}'
    name = input().lower().title().split()
    name = ' '.join(name)
    s1 = int(input())
    s2 = int(input())
    s3 = int(input())
    a.append(Average_grade(id,name,s1,s2,s3))
a = sorted(a,key = lambda x: (-x.s,x.name))
for i in range(len(a)):
    a[i].output()
    if i == 0:
        print(i + 1)
    else:
        if a[i].s == a[i - 1].s:
            print(i)
        else:
            print(i + 1)
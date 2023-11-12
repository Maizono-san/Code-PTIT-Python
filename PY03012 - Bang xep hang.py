class Sinhvien:
    def __init__(self,name,correct,submit):
        self.name = name
        self.correct = correct
        self.submit = submit
    def output(self):
        print(self.name,self.correct,self.submit)

a = []
for t in range(int(input())):
    name = input()
    correct,submit = [int(x) for x in input().split()]
    a.append(Sinhvien(name,correct,submit))

a.sort(key = lambda x: (-x.correct,x.submit,x.name))
for i in a:
    i.output()
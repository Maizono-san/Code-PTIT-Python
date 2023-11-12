class Subject:
    def __init__(self,code,name,test):
        self.code = code
        self.name = name
        self.test = test
    def __str__(self):
        return self.code + ' ' + self.name + ' ' + self.test

def process():
    for i in range(t - 1):
        for j in range(i + 1,t):
            if a[i].code > a[j].code:
                a[i],a[j] = a[j],a[i]
        

t = int(input())
a = []
for i in range(t):
    code = input()
    name = input()
    test = input()
    a.append(Subject(code,name,test))
process()
for i in range(t):
    print(a[i])
b = set([a.lower() for a in input().split()])
c = set([a.lower() for a in input().split()])
print(' '.join((sorted(b.union(c)))))
print(' '.join(sorted(b.intersection(c))))
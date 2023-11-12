arr = []
a = set()
while len(arr) < 10:
    arr.extend(input().split())
for i in range(len(arr)):
   a.add(int(arr[i]) % 42)
print(len(a))

t = int(input())
for i in range(t):
    s1 = sorted(list(input()))
    s2 = sorted(list(input()))
    if s1 == s2:
        print(f"Test {i + 1}: YES")
    else:
        print(f"Test {i + 1}: NO")
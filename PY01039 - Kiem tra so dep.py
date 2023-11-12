t = int(input())
for i in range(t):
   s = input()
   c = 0
   j,k = 0,0
   if len(s) % 2 == 0:
      while j < len(s) - 2:
         if s[j] != s[j + 2] or s[j + 1] != s[j + 3]:
            c = 1
            print("NO")
            break
         j += 2
      if c == 0:
         print("YES")
   else:
      while k < len(s) - 3:
         if s[k] != s[k + 2] or s[k + 1] != s[k + 3]:
            c = 1
            break
         k += 2
      if c == 0 and s[len(s)-1] == s[len(s)-3]:
         print("YES")
      else:
         print("NO")
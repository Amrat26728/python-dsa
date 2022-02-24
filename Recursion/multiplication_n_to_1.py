def multiNTo1(n):
     if n == 1:
          return 1
     return n * multiNTo1(n - 1)

print(multiNTo1(6))
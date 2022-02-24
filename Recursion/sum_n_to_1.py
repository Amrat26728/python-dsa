def sumNTo1(n):
     if n == 0:
          return 0
     return n + sumNTo1(n - 1)

print(sumNTo1(5))
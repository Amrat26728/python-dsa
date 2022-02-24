def productOfDigits(n):
     if n < 10:
          return n
     return (n%10) * productOfDigits(int(n/10))

print(productOfDigits())
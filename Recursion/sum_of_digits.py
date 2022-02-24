def sumOfDigits(n):
     if n < 10:
          return n
     return (n % 10) + sumOfDigits(int(n/10))

print(sumOfDigits(123456))
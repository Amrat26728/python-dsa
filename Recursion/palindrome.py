def reverse_num(n):
     if n < 10:
          return n
     return str(n%10)+str(reverse_num(n//10))

def palindrome(n):
     return n == int(reverse_num(n))

print(palindrome(12321))
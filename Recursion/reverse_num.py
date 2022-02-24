def count_zeros(n, count):
     if n < 10:
          return count
     if n%10 == 0:
          return count_zeros(n//10, count+1)
     return count_zeros(n//10, count)

print(count_zeros(3050302, 0))
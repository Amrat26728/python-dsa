num = int(input("Enter number: "))

if type(num) == int:
     n1 = 1
     n2 = num
     while n1<=n2:
          mid = int((n1+n2)/2)
          if (mid*mid)==num:
               print("Perfect square is: ", mid)
               break

          elif (mid*mid)<num:
               n1 = mid

          elif (mid*mid)>num:
               n2 = mid
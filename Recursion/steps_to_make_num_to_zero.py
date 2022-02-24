# def make_num_to_zero(n, count):
#      if n == 0:
#           return count
#      if n%2 == 0:
#           return make_num_to_zero(n/2, count + 1)
#      return make_num_to_zero(n-1, count + 1)

# print(make_num_to_zero(8, 0))

class Solution:
    def numberOfSteps(self, num: int) -> int:
        return self.make_num_to_zero(num, 0)
        
    def make_num_to_zero(self, n, count):
        if n == 0:
            return count
        if n%2 == 0:
            return self.make_num_to_zero(n/2, count + 1)
        return self.make_num_to_zero(n-1, count + 1)
    
num = 14
print(Solution().numberOfSteps(num))
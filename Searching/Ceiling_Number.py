from array import array 

def ceiling_num(arr, target):
     start = 0;
     end = len(arr) - 1
     while start <= end:
          mid = int((start + end)/2)
          if arr[mid] == target:
               return mid

          elif arr[mid] < target:
               start = mid + 1

          elif arr[mid] > target:
               end = mid - 1

     return start

arr = array('i', [8, 9, 11, 13, 16, 18, 20])
target = 19
print(ceiling_num(arr, target))
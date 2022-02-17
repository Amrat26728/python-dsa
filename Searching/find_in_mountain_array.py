from array import array

class Find_in_mountain_array:
     def find_target_element(self, arr, target):
          start = 0
          end = len(arr) - 1
          index = -1
          while start <= end:
               mid = int((start + end)/2)
               if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                    index = self.binary_search(0, mid, target, arr)
                    break
               elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                    start = mid + 1
               elif arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
                    end = mid - 1

          if index < 0:
               return self.binary_search(mid+1, len(arr)-1, target, arr)
          else:
               return index

     def binary_search(self, start, end, target, arr):
          while start <= end:
               mid = int((start + end)/2)
               if arr[mid] == target:
                    return mid
               elif arr[mid] < target:
                    start = mid + 1
               elif arr[mid] > target:
                    end = mid - 1
          return -1

arr = array('i', [1,2,3,5,3,1,4])
target = 3
print(Find_in_mountain_array().find_target_element(arr, target))
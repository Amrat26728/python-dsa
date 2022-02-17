from array import array

def peak_element(arr, target):
     start = 0
     end = len(arr) - 1
     while start < end:
          mid = int((start + end)/2)
          if arr[mid] > arr[mid+1]:
               end = mid
          else:
               start = mid + 1
     return start

def binary_search(start, end, arr, target):
     if arr[start] > target and arr[end] > target:
          return -1
     else:
          while start <= end:
               mid = int((start + end)/2)
               if arr[mid] == target:
                    return mid
               elif arr[mid] < target:
                    start = mid + 1
               elif arr[mid] > target:
                    end = mid - 1
          return -1

arr = array('i', [4, 5, 6, 7, 0, 1, 2])
target = 0
peak_ele = peak_element(arr, target)
target_index = binary_search(0, peak_ele, arr, target)
if target_index == -1:
     print(binary_search(peak_ele + 1, len(arr) - 1, arr, target))
else:
     print(target_index)
from array import array

arr = array('i', [1,2,1,3,5,6,4])

def search_Mountain_Array(arr):
     if len(arr) < 3:
          return -1
     else:
          start = 0
          end = len(arr) - 1
          while start <= end:
               mid = int((start + end)/2)
               if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
                    return arr[mid]
               elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
                    start = mid + 1
               elif arr[mid] > arr[mid + 1] and arr[mid] < arr[mid - 1]:
                    end = mid - 1

print(search_Mountain_Array(arr))
from array import array

arr = array('i', [3,1,5,4,2])

print("Before sorting: ", arr)

for i in range(len(arr)):
     checker = True
     for j in range(len(arr)-i-1):
          if arr[j]>arr[j+1]:
               arr[j],arr[j+1] = arr[j+1],arr[j]
               checker = False

     if checker:
          break

print("After sorting: ", arr)
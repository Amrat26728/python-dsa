from array import array

arr = array('i', [5, 3, 4, 1, 2])

print("Before Sorting: ", arr)

for i in range(len(arr)-1):
    checker = True
    for j in range(i+1, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            checker = False
        if checker:
            break

print("After Sorting: ", arr)

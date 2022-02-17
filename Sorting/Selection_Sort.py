from array import array

arr = array('i', [3, 45, 21, 4, 1, -11, 56, 32])

print("Before Sorting: ", arr)
for i in range(len(arr)-1):    # this outer loop is for passes
    index = 0
    max = arr[index]
    # this inner loop is find max element in the array.
    for j in range(len(arr)-1-i):
        if max < arr[j+1]:
            max = arr[j+1]
            index = j+1
    # swaping the two elements.
    arr[len(arr)-1-i], arr[index] = arr[index], arr[len(arr)-1-i]

print("After Sorting: ", arr)
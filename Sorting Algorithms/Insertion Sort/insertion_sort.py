def insertion_sort(arr):
    # for every index in array
    for i in range(1, len(arr)):
        # set current values and position
        currentvalue = arr[i]
        position = i
        
        # sorted sublist
        while position > 0 and arr[position-1]>currentvalue:
            arr[position] = arr[position-1]
            position = position - 1
            
        arr[position] = currentvalue
    return arr

arr = [3,2,13,4,6,5,7,8,1,20]
print("Output: ", insertion_sort(arr))

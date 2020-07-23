def selection_sort(arr):
    
    # for every slot in array
    for fillslot in range(len(arr)-1,0,-1):
        positionOfMax = 0
        
        # for every set of 0 to fillslot+1
        for location in range(1,fillslot+1):
            # set maximum's location
            if arr[location]>arr[positionOfMax]:
                positionOfMax = location
            
        temp = arr[fillslot]
        arr[fillslot] = arr[positionOfMax]
        arr[positionOfMax] = temp
    return arr

arr = [3,2,13,4,6,5,7,8,1,20]
print("Output: ", selection_sort(arr))
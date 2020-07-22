# merge sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr)/2)
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = 0 # for left half
        j = 0 # for right half
        k = 0 # all list
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k = k + 1
            
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
    return arr


arr = [3,2,13,4,6,5,7,8,1,20]
print("Output: ", merge_sort(arr) )
# Output:  [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
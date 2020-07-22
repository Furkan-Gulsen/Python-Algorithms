# Bubble sort example

def bubbleSortAlgorithm(arr):
    # for every element (arranged backwards)
    for n in range(len(arr)-1, 0, -1): # [20,19,18,17 .... 0]
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
                
    return arr

arr = [3,2,13,4,6,5,7,8,20]
print("Output: ", bubbleSortAlgorithm(arr))
## BUBBLE SORT - SORTING ALGORITHMS

- It sorts two consecutive values ​​in a list and continues this process until the whole list becomes sequential.

```python
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
```
output:
```
[2, 3, 4, 5, 6, 7, 8, 13, 20]
```

<img src="https://www.productplan.com/uploads/bubble-sort-1024x683-2.png" />

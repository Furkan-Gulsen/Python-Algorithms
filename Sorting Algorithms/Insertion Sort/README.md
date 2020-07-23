## INSERTION SORT

- Sub list is used.
- The first value is a sublist element and is sequential because it already has a single value.
- The remaining values ​​in this sub list are added by comparison.

```python
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
```
output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
```

<img src="https://miro.medium.com/max/3204/1*5t5q_OLP-kGwQyblAN-nog.png" />

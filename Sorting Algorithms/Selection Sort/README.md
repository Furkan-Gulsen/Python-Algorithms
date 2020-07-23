## SELECTION SORT

- I have an unordered list.
- I find the smallest value in this list and set it to index 0.
- Then I find the next smallest value and continue my search.

```python
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
```
output:
```
[1, 2, 3, 4, 5, 6, 7, 8, 13, 20]
```


<img src="https://lh3.googleusercontent.com/proxy/jbSWXUD7nCXlB6UvnYwu70Uj5CrhrQWJs5JixA5vu7HD-yVxUF0yo29lUWu0-GI00cC1XPE1B43YsTPeHk2m0H5Bxd2cAg4Ju_4s4kYs-oT1mmKkR_E996kieZQOhNoqlVjmWDOTCMk"/>

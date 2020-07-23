# COUNTING SORT

- Counting sort is a sorting technique based on keys between a specific range. 
- It works by counting the number of objects having distinct key values (kind of hashing). 
- Then doing some arithmetic to calculate the position of each object in the output sequence.

```python
def counting_sort(array, maxval):
    n = len(array)
    m = maxval + 1
    count = [0] * m  # init with zeros
    for a in array:
        count[a] += 1  # count occurences
    i = 0
    for a in range(m): # emit
        for c in range(count[a]): # emit "count[a]" copies of "a"
            array[i] = a
            i += 1
    return array


arr = [1,4,7,2,1,3,2,1,4,2,3,2,1]
print("Output: ", counting_sort(arr, 7))
```
output:
```
[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 7]
```

<img src="https://cdn.programiz.com/sites/tutorial2program/files/Counting-sort-4_1.png" />
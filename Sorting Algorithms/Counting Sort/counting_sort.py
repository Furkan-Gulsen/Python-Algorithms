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
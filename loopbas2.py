# 1.
def biggie_size(arr):
    for x in range(len(arr)):
        if arr[x] > 0:
            arr[x] = "big"
    return arr

print (biggie_size([-1, 3, 5, -5]))

# 2.
def count_positives(arr):
    count = 0
    for x in range(len(arr)):
        if arr[x] > 0:
            count += 1
    arr[-1] = count
    return arr

print (count_positives([1, 6, -4, -2, -7, -2]))

# 3.
def sum_total(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum

print (sum_total([6, 3, -2]))

# 4.
def average(arr):
    return sum_total(arr)/len(arr)

print (average([1, 2, 3, 4]))

# 5.
def length(arr):
    len = 0
    for x in arr:
        len += 1
    return len

print (length([37, 2, 1, -9]))

# 6.
def minimum(arr):
    if len(arr) == 0:
        return False
    else:
        min = arr[0]
        for x in arr:
            if x < min:
                min = x
        return min

print (minimum([37, 2, 1, -9]))

# 7. 
def maximum(arr):
    if len(arr) == 0:
        return False
    else:
        max = arr[0]
        for x in arr:
            if x > max:
                max = x
        return max

print(maximum([37, 2, 1, -9]))

# 8.
def ultimate_analysis(arr):
    listdict = {
        "sumTotal": sum_total(arr),
        "average": average(arr),
        "minimum": minimum(arr),
        "maximum": maximum(arr),
        "length": length(arr)
    }
    return listdict

print(ultimate_analysis([37, 2, 1, -9]))

# 9.
def reverse_list(arr):
    listdict = {}
    for x in range(len(arr)):
        listdict[x] = arr[x]
    counter = -1
    for x in range(len(arr)):
        arr[counter] = listdict[x]
        counter -= 1
    return arr

print(reverse_list([37, 2, 1, -9]))
def cutTheSticks(arr):
    # Write your code here
    result = []
    while len(arr) != 0:
        arrmin = min(arr)
        arr = [arr[i]-arrmin for i in range(len(arr))]
        # noofcuts += len(arr)
        result.append(len(arr))
        while 0 in arr:
            arr.remove(0)
    return result


arr = [5, 4, 4, 2, 2, 8]
result = cutTheSticks(arr)
print(result)

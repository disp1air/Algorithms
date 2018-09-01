def recurs_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recurs_sum(arr[1:])


print(recurs_sum([1, 2, 5, 22]))

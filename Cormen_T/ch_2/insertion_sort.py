l = [6, 2, 4]

def insertion_sort(arr):
    for index in range(1, len(arr)):
        value = arr[index]
        i = index - 1

        while i >= 0 and arr[i] > arr[index]:
            arr[index], arr[i] = arr[i], arr[index]
            i -= 1

    return arr

    # for n in range(1,len(arr)):
    #     i = n - 1 
    #     while (i > -1) and arr[i+1] < arr[i]:
    #         arr[i+1], arr[i] = arr[i], arr[i+1]
    #         i -= 1
    # return(arr)    

print(insertion_sort(l))
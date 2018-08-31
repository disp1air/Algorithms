from find_smallest import find_smallest

def selection_sort(arr):
    sorted_arr = []
  
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(smallest)
        arr.remove(smallest)
  
    return sorted_arr
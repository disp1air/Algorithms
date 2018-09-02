def firstDuplicate(a):
    """
    Given an array a that contains only numbers in the range from 1 to a.length, 
    find the first duplicate number for which the second occurrence has the minimal index. 
    In other words, if there are more than 1 duplicated numbers, return the number 
    for which the second occurrence has a smaller index than the second occurrence of 
    the other number does. If there are no such elements, return -1.

    For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.
    There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index 
    than the second occurrence of 2 does, so the answer is 3.

    For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1    
    """

    arr = []
    for i in a:
        if i not in arr:
            arr.append(i)
        elif i in arr:
            return i
    
    return -1

# def firstDuplicate(a):
#     mySet=set()
#     for el in a:
#         if el in mySet:
#             return el
#         mySet.add(el)
#     return -1

# def firstDuplicate(a):
#     for i in a:
#         a[abs(i)-1] *= -1
#         if a[abs(i)-1] > 0:
#             return abs(i)
#     return -1
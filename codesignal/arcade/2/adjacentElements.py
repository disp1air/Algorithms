def adjacentElements(inputList):
    """
    Given an array of integers, find the pair of adjacent elements 
    that has the largest product and return that product.
    """
    return max([inputList[i] * inputList[i+1] for i in range(len(inputList)-1)])

# def adjacentElementsProduct(inputArray):
#     return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

# def adjacentElementsProduct(inputArray):
#     return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))

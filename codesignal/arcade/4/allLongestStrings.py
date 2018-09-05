def allLongestStrings(inputList):
    """
    Given an array of strings, return another array containing all of its longest strings.

    For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
    allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
    """
    maxLen = 0

    for x in range(len(inputList)):
        maxLength = len(inputList[x])
        if maxLength > maxLen:
            maxLen = maxLength

    return [inputList[i] for i in range(len(inputList)) if len(inputList[i]) == maxLen]

# def allLongestStrings(inputArray):
#     m = max(len(s) for s in inputArray)
#     r = [s for s in inputArray if len(s) == m]
#     return r


# def allLongestStrings(inputArray):
#     lengthArray = []
#     for strings in inputArray: 
#         lengthArray.append(len(strings))
#     maxLength = max(lengthArray)
#     maxStrings = []
#     for strings in inputArray: 
#         if len(strings) == maxLength: 
#             maxStrings.append(strings)
#     return maxStrings
        

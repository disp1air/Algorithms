def checkPalindrome(s):
    """
    Given the string, check if it is a palindrome.
    A palindrome is a string that reads the same left-to-right and right-to-left.
    """
    myStr = s[::-1]
    res = True if myStr == s else False
    return res

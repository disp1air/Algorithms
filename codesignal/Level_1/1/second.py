def firstNotRepeatingCharacter(s):
    """
    Given a string s, find and return the first instance 
    of a non-repeating character in it. If there is no such 
    character, return '_'.
    
    For s = "abacabad", the output should be 
    firstNotRepeatingCharacter(s) = 'c'.

    There are 2 non-repeating characters in the string: 'c' and 'd'.
    Return c since it appears in the string first.

    For s = "abacabaabacaba", the output should be
    firstNotRepeatingCharacter(s) = '_'.

    There are no characters in this string that do not repeat.
    """

    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'
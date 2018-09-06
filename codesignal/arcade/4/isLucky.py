def isLucky(n):
    """
    Ticket numbers usually consist of an even number of digits. 
    A ticket number is considered lucky if the sum of the first half 
    of the digits is equal to the sum of the second half.

    Given a ticket number n, determine if it's lucky or not.
    """
    d = map(int, str(n))
    m = len(d) / 2
    return sum(d[:m]) == sum(d[m:])

def isLucky(n):
    s = str(n)
    pivot = len(s)//2
    left, right = s[:pivot], s[pivot:]
    return sum(map(int, left)) == sum(map(int, right))

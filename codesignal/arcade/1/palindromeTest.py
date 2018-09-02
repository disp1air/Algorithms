import unittest
from palindrome import checkPalindrome


class palindromeTestCase(unittest.TestCase):
    def test_first_duplicate(self):        
        result = checkPalindrome('aabaa')
        self.assertEqual(result, True)

        result = checkPalindrome('abac')
        self.assertEqual(result, False)

        result = checkPalindrome('a')
        self.assertEqual(result, True)

        result = checkPalindrome('az')
        self.assertEqual(result, False)

        result = checkPalindrome('abacaba')
        self.assertEqual(result, True)

        result = checkPalindrome('aaabaaaa')
        self.assertEqual(result, False)

        result = checkPalindrome('zzzazzazz')
        self.assertEqual(result, False)
        
        result = checkPalindrome('hlbeeykoqqqqokyeeblh')
        self.assertEqual(result, True)

        result = checkPalindrome('hlbeeykoqqqokyeeblh')
        self.assertEqual(result, True)

unittest.main()

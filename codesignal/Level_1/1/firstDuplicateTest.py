import unittest
from firstDuplicate import firstDuplicate


class FirstDuplicateTestCase(unittest.TestCase):
    def test_first_duplicate(self):        
        result = firstDuplicate([2, 1, 3, 5, 3, 2])
        self.assertEqual(result, 3)

        result = firstDuplicate([2, 4, 3, 5, 1])
        self.assertEqual(result, -1)

        result = firstDuplicate([1])
        self.assertEqual(result, -1)

        result = firstDuplicate([2, 2])
        self.assertEqual(result, 2)

        result = firstDuplicate([2, 1])
        self.assertEqual(result, -1)

        result = firstDuplicate([2, 1, 3])
        self.assertEqual(result, -1)

        result = firstDuplicate([2, 3, 3])
        self.assertEqual(result, 3)

        result = firstDuplicate([3, 3, 3])
        self.assertEqual(result, 3)

        result = firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])
        self.assertEqual(result, 6)
        
        result = firstDuplicate([10, 6, 8, 4, 9, 1, 7, 2, 5, 3])
        self.assertEqual(result, -1)
        
        result = firstDuplicate([1, 1, 2, 2, 1])
        self.assertEqual(result, 1)


unittest.main()

import unittest
from find_smallest import find_smallest


class FindSmallestTestCase(unittest.TestCase):
    def test_find_smallest(self):
        arr = [4, 5, 2, 1, 8]
        result = find_smallest(arr)
        self.assertEqual(result, 1)

        arr = [2, 6, 0, 4, 1, 6]
        result = find_smallest(arr)
        self.assertEqual(result, 0)

        arr = [3, 5, 0, -4, 5]
        result = find_smallest(arr)
        self.assertEqual(result, -4)


unittest.main()

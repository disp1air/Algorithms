import unittest
from binary_search import binary_search

list = [0, 1, 2, 3, 4, 5, 6]


class SearchTestCase(unittest.TestCase):
    def test_binary_search(self):
        result = binary_search(list, 1)
        self.assertEqual(result, 1)

        result = binary_search(list, 6)
        self.assertEqual(result, 6)

        result = binary_search(list, 11)
        self.assertEqual(result, None)

        result = binary_search(list, 0)
        self.assertEqual(result, 0)


unittest.main()

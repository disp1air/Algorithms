import unittest
from selection_sort import selection_sort


class SelectionSortTestCase(unittest.TestCase):
    def test_selection_sort(self):
        arr = [3, 1, 4, 2, 5, 0]
        result = selection_sort(arr)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5])

        arr = [1, 3, 2, 0, 6, 9, 8]
        result = selection_sort(arr)
        self.assertEqual(result, [0, 1, 2, 3, 6, 8, 9])

        arr = [1, -3, -2, 6, 6, 9, 6]
        result = selection_sort(arr)
        self.assertEqual(result, [-3, -2, 1, 6, 6, 6, 9])


unittest.main()

import unittest
from adjacentElements import adjacentElements


class AdjacentElementsTestCase(unittest.TestCase):
    def test_adjacent_elements(self):
        result = adjacentElements([3, 6, -2, -5, 7, 3])
        self.assertEqual(result, 21)

        result = adjacentElements([-1, -2])
        self.assertEqual(result, 2)

        result = adjacentElements([5, 1, 2, 3, 1, 4])
        self.assertEqual(result, 6)

        result = adjacentElements([1, 2, 3, 0])
        self.assertEqual(result, 6)
        
        result = adjacentElements([9, 5, 10, 2, 24, -1, -48])
        self.assertEqual(result, 50)

        result = adjacentElements([5, 6, -4, 2, 3, 2, -23])
        self.assertEqual(result, 30)
        
        result = adjacentElements([4, 1, 2, 3, 1, 5])
        self.assertEqual(result, 6)
        
        result = adjacentElements([-23, 4, -3, 8, -12])
        self.assertEqual(result, -12)
        
        result = adjacentElements([1, 0, 1, 0, 1000])
        self.assertEqual(result, 0)

unittest.main()
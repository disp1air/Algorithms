import unittest
from shapeArea import shapeArea


class shapeAreaTestCase(unittest.TestCase):
    def test_shape_area(self):
        result = shapeArea(1)
        self.assertEqual(result, 1)

        result = shapeArea(2)
        self.assertEqual(result, 5)

        result = shapeArea(3)
        self.assertEqual(result, 13)

        result = shapeArea(4)
        self.assertEqual(result, 25)
        
        result = shapeArea(5)
        self.assertEqual(result, 41)
unittest.main()
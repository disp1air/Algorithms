import unittest
from centuryFromYear import centuryFromYear

class CenturyFromYearTestCase(unittest.TestCase):
    def test_century(self):
        result = centuryFromYear(1905)
        self.assertEqual(result, 20)

        result = centuryFromYear(1700)
        self.assertEqual(result, 17)

        result = centuryFromYear(1988)
        self.assertEqual(result, 20)

        result = centuryFromYear(2000)
        self.assertEqual(result, 20)

        result = centuryFromYear(2100)
        self.assertEqual(result, 21)

        result = centuryFromYear(200)
        self.assertEqual(result, 2)

        result = centuryFromYear(374)
        self.assertEqual(result, 4)

        result = centuryFromYear(45)
        self.assertEqual(result, 1)

        result = centuryFromYear(8)
        self.assertEqual(result, 1)

unittest.main()
import unittest
from increasingSeq import almostIncreasingSequence

class IncreasingSeqTestCase(unittest.TestCase):
    def test_increasing_seq(self):
        result = almostIncreasingSequence([1, 3, 2, 1])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([1, 3, 2])
        self.assertEqual(result, true)

        result = almostIncreasingSequence([1, 2, 1, 2])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([1, 4, 10, 4, 2])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([10, 1, 2, 3, 4, 5])
        self.assertEqual(result, true)

        result = almostIncreasingSequence([1, 1, 1, 2, 3])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([0, -2, 5, 6])
        self.assertEqual(result, true)

        result = almostIncreasingSequence([1, 2, 3, 4, 5, 3, 5, 6])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([40, 50, 60, 10, 20, 30])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([1, 1])
        self.assertEqual(result, true)

        result = almostIncreasingSequence([1, 2, 5, 3, 5])
        self.assertEqual(result, true)

        result = almostIncreasingSequence([1, 2, 5, 5, 5])
        self.assertEqual(result, false)

        
        result = almostIncreasingSequence([10, 1, 2, 3, 4, 5, 6, 1])
        self.assertEqual(result, false)

        result = almostIncreasingSequence([1, 2, 3, 4, 3, 6])
        self.assertEqual(result, true)

        result = almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6])
        self.assertEqual(result, true)

unittest.main()
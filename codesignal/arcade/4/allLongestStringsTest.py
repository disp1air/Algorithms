import unittest
from allLongestStrings import allLongestStrings

class AllLongestStringsTestCase(unittest.TestCase):
    def test_all_longest_string(self):
        inputList = ["aba", "aa", "ad", "vcd", "aba"]
        outputList = ["aba", "vcd", "aba"]
        result = allLongestStrings(inputList)
        self.assertEqual(result, outputList)

        inputList = ["aa"]
        outputList = ["aa"]
        result = allLongestStrings(inputList)
        self.assertEqual(result, outputList)

        inputList = ["abc", "eeee", "abcd", "dcd"]
        outputList = ["eeee" , "abcd"]
        result = allLongestStrings(inputList)
        self.assertEqual(result, outputList)

        inputList = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
        outputList = ["zzzzzz", "abcdef", "aaaaaa"]
        result = allLongestStrings(inputList)
        self.assertEqual(result, outputList)


unittest.main()
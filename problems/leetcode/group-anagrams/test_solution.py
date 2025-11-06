import unittest
import sys
import os
from typing import List

# Add the current directory to the path to import solution
sys.path.insert(0, os.path.dirname(__file__))
from solution import Solution

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = self.solution.groupAnagrams(strs)
        # Sort each group and the groups themselves for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        expected = [["bat"], ["eat","tea","ate"], ["tan","nat"]]
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        self.assertEqual(result_sorted, expected_sorted)
    
    def test_example_2(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
